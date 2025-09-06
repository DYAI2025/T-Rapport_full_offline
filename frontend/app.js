// TransRapport - Minimal-Integration mit Backend /process

class TransRapportApp {
  constructor() {
    this.isRecording = false;
    this.timerId = null;
    this.startedAt = 0;
    this.transcriptionData = [];   // [{speaker, text, ts}]
    this.markerEvents = [];        // from backend
    
    // DOM Elements
    this.$disp = document.getElementById('transcription-display');
    this.$markers = document.getElementById('marker-list');
    this.$timer = document.getElementById('session-timer');
    this.$file = document.getElementById('file-input');
    this.$modalBody = document.getElementById('full-transcript');
    this.$markerCount = document.getElementById('marker-count');
    this.$sessionId = document.getElementById('session-id');
    this.$statusDot = document.getElementById('status-indicator');
    this.$statusText = document.getElementById('status-text');
    this.$fileInfo = document.getElementById('file-info');
    
    this.bind();
    this.checkHealth();
  }

  bind() {
    document.getElementById('btn-start').addEventListener('click', () => this.start());
    document.getElementById('btn-pause').addEventListener('click', () => this.pause());
    document.getElementById('btn-stop').addEventListener('click', () => this.stopAndProcess());
    
    this.$file.addEventListener('change', (e) => this.handleFileSelect(e));
    
    // Modal controls
    document.getElementById('btn-full-transcript').addEventListener('click', () => this.showFullTranscript());
    document.getElementById('close-transcript').addEventListener('click', () => this.closeModal());
    
    // Export buttons
    document.querySelectorAll('.btn-export').forEach(btn => {
      btn.addEventListener('click', (e) => this.exportTranscript(e.target.dataset.format));
    });
  }

  async checkHealth() {
    try {
      const response = await fetch('/healthz');
      if (response.ok) {
        const data = await response.json();
        this.setConnectionStatus(true);
      } else {
        throw new Error('Health check failed');
      }
    } catch (error) {
      this.setConnectionStatus(false);
    }
  }

  setConnectionStatus(isOnline) {
    this.$statusDot.className = `status-dot ${isOnline ? 'online' : 'offline'}`;
    this.$statusText.textContent = isOnline ? 'Online' : 'Offline';
  }

  handleFileSelect(event) {
    const file = event.target.files[0];
    if (file) {
      this.$fileInfo.innerHTML = `
        <strong>Ausgewählt:</strong> ${file.name}<br>
        <small>Größe: ${(file.size / 1024 / 1024).toFixed(1)} MB</small>
      `;
    }
  }

  start() {
    if (!this.$file.files || !this.$file.files[0]) {
      this.toast('Bitte zuerst eine Audiodatei auswählen.');
      return;
    }
    if (this.isRecording) return;
    
    this.isRecording = true;
    this.startedAt = Date.now();
    this.tickTimer();
    this.timerId = setInterval(() => this.tickTimer(), 500);
    this.simulateLiveFeed();
    this.setRecordingUI(true);
    
    // Session ID setzen
    const sessionId = `ui-${Date.now()}`;
    this.$sessionId.textContent = `Session: ${sessionId}`;
  }

  pause() {
    if (!this.isRecording) return;
    this.isRecording = false;
    clearInterval(this.timerId);
    this.setRecordingUI(false);
  }

  formatMMSS(ms) {
    const s = Math.floor(ms / 1000);
    const mm = String(Math.floor(s / 60)).padStart(2, '0');
    const ss = String(s % 60).padStart(2, '0');
    return `${mm}:${ss}`;
  }

  tickTimer() {
    const elapsed = Date.now() - this.startedAt;
    if (this.$timer) this.$timer.textContent = this.formatMMSS(elapsed);
  }

  async stopAndProcess() {
    clearInterval(this.timerId);
    this.setRecordingUI(false);
    this.isRecording = false;

    // Export-Optionen anzeigen
    document.getElementById('export-options').style.display = 'block';

    // Datei an /process schicken
    const file = this.$file.files[0];
    if (!file) { 
      this.toast('Keine Datei gewählt.'); 
      return; 
    }

    const fd = new FormData();
    fd.append('file', file);

    let resp;
    try {
      const ctrl = new AbortController();
      const t = setTimeout(() => ctrl.abort(), 12000); // 12s Hard-Timeout
      resp = await fetch('/process', { 
        method: 'POST', 
        body: fd, 
        signal: ctrl.signal 
      });
      clearTimeout(t);
    } catch (e) {
      this.toast('Verarbeitung überschritt das Zeitlimit oder Backend offline.');
      return;
    }

    if (!resp.ok) {
      const msg = (await resp.text()).trim();
      this.toast(msg || 'Verarbeitung fehlgeschlagen.');
      return;
    }

    const data = await resp.json();
    // Erwartet: { session, input, events: [{type, score, ts, ...}] }
    this.markerEvents = Array.isArray(data.events) ? data.events : [];
    this.renderMarkers(this.markerEvents);
    this.buildFullTranscript();
    this.toast('Analyse abgeschlossen.');
    
    // Session ID aus Backend übernehmen
    if (data.session) {
      this.$sessionId.textContent = `Session: ${data.session}`;
    }
  }

  renderMarkers(events) {
    if (!this.$markers) return;
    
    // Placeholder entfernen
    const placeholder = this.$markers.querySelector('.marker-placeholder');
    if (placeholder) placeholder.remove();
    
    const frag = document.createDocumentFragment();
    const byType = {};
    
    events.forEach(e => {
      byType[e.type] = (byType[e.type] || 0) + 1;
    });
    
    // Counter aktualisieren
    const totalEvents = events.length;
    this.$markerCount.textContent = `${totalEvents} Events`;
    
    // Marker-Liste rendern
    Object.entries(byType).forEach(([type, count]) => {
      const li = document.createElement('li');
      li.className = `marker-item marker-${type}`;
      li.innerHTML = `
        <span class="marker-type">${type.toUpperCase()}</span>
        <span class="marker-count-badge">${count}</span>
      `;
      frag.appendChild(li);
    });
    
    this.$markers.innerHTML = '';
    this.$markers.appendChild(frag);
  }

  buildFullTranscript() {
    if (!this.$modalBody) return;
    
    // Einfache Transkript-Ansicht mit Marker-Info
    let html = '';
    
    if (this.transcriptionData.length > 0) {
      html = this.transcriptionData.map(row => `
        <div class="line">
          <div class="meta">
            <span class="spk">${row.speaker || 'SPEAKER'}</span> 
            <span class="ts">${row.ts || ''}</span>
          </div>
          <p>${this.escape(row.text)}</p>
        </div>
      `).join('');
    } else {
      // Fallback: Marker-Events als Transkript-Ersatz
      if (this.markerEvents.length > 0) {
        html = `
          <div class="marker-summary">
            <h4>Erkannte Marker Events:</h4>
            ${this.markerEvents.map(event => `
              <div class="marker-entry">
                <strong>${event.type}</strong> bei ${(event.ts || 0).toFixed(1)}s 
                (Score: ${(event.score || 0).toFixed(2)})
              </div>
            `).join('')}
          </div>
        `;
      } else {
        html = '<p class="no-content">Noch keine Transkription verfügbar</p>';
      }
    }
    
    this.$modalBody.innerHTML = html;
  }

  simulateLiveFeed() {
    // Live-Animation für das Transkriptions-Display
    this.$disp.innerHTML = '';
    
    const liveText = [
      'Starte Live-Transkription...',
      'Audio wird analysiert...',
      'Marker-Erkennung aktiviert...',
      'Verarbeitung läuft...',
      '[Echte Transkription erscheint nach Stopp]'
    ];
    
    liveText.forEach((text, index) => {
      setTimeout(() => {
        // Speichere für spätere Vollansicht
        this.transcriptionData.push({
          speaker: 'SYSTEM',
          text: text,
          ts: this.formatMMSS((index + 1) * 1000)
        });
        
        const lineElement = document.createElement('div');
        lineElement.className = 'transcript-line current';
        lineElement.textContent = text;
        
        this.$disp.appendChild(lineElement);
        this.$disp.scrollTop = this.$disp.scrollHeight;
        
        // Animation entfernen
        setTimeout(() => {
          lineElement.classList.remove('current');
        }, 500);
        
      }, index * 1200);
    });
  }

  setRecordingUI(on) {
    document.body.classList.toggle('recording', !!on);
    
    // Button states
    const btnStart = document.getElementById('btn-start');
    const btnPause = document.getElementById('btn-pause');
    const btnStop = document.getElementById('btn-stop');
    
    btnStart.disabled = on;
    btnPause.disabled = !on;
    btnStop.disabled = !on;
    
    if (on) {
      btnPause.innerHTML = '<span class="btn-icon">⏸</span><span>Pause</span>';
    } else {
      btnPause.innerHTML = '<span class="btn-icon">⏸</span><span>Pause</span>';
    }
  }

  // Modal Functions
  showFullTranscript() {
    document.getElementById('document-title').textContent = 
      `Transkription vom ${new Date().toLocaleDateString('de-DE')}`;
    document.getElementById('doc-session-id').textContent = 
      this.$sessionId.textContent.replace('Session: ', '') || '-';
    document.getElementById('doc-duration').textContent = this.$timer.textContent;
    
    this.buildFullTranscript();
    document.getElementById('transcript-modal').style.display = 'block';
  }

  closeModal() {
    document.getElementById('transcript-modal').style.display = 'none';
  }

  exportTranscript(format) {
    if (format === 'txt') {
      // Einfacher Text-Export
      const content = this.transcriptionData
        .map(row => `${row.speaker} [${row.ts}]: ${row.text}`)
        .join('\n');
      
      const blob = new Blob([content], { type: 'text/plain' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `transcript-${Date.now()}.txt`;
      a.click();
      URL.revokeObjectURL(url);
    } else {
      this.toast(`Export als ${format.toUpperCase()} kommt in einer zukünftigen Version.`);
    }
  }

  escape(s) {
    return String(s).replace(/[&<>"']/g, m => ({
      '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
    }[m]));
  }

  toast(msg) {
    console.log('[UI]', msg);
    
    // Einfache Toast-Nachricht
    const toast = document.createElement('div');
    toast.style.cssText = `
      position: fixed; top: 20px; right: 20px; z-index: 9999;
      background: rgba(0,0,0,0.8); color: white; padding: 12px 20px;
      border-radius: 8px; font-size: 14px; backdrop-filter: blur(10px);
    `;
    toast.textContent = msg;
    document.body.appendChild(toast);
    
    setTimeout(() => {
      toast.remove();
    }, 3000);
  }
}

// App initialisieren
window.addEventListener('DOMContentLoaded', () => new TransRapportApp());