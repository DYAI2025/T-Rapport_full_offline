# TransRapport API Documentation

## API Overview

The TransRapport API provides RESTful endpoints for audio processing and marker detection. The system operates entirely offline and processes therapy sessions in real-time or batch mode.

**Base URL**: `http://localhost:8765`  
**Version**: 3.4  
**Schema**: LEAN.DEEP 3.4 Marker System

---

## Authentication

No authentication required for local deployment. All endpoints are publicly accessible on localhost.

---

## Endpoints

### GET /

**Description**: Root endpoint providing API information.

**Response**:
```json
{
  "ok": true,
  "hint": "Use /healthz or POST /process"
}
```

**Status Codes**:
- `200 OK`: Always successful

---

### GET /healthz

**Description**: System health check and configuration status.

**Response**:
```json
{
  "status": "ok",
  "offline": true,
  "models_path": "./models/ct2",
  "bundle": "./bundles/SerapiCore_1.0.yaml"
}
```

**Fields**:
- `status`: System operational status (`ok` | `error`)
- `offline`: Indicates offline-first operation (always `true`)
- `models_path`: Path to STT models directory
- `bundle`: Path to active marker bundle

**Status Codes**:
- `200 OK`: System operational
- `503 Service Unavailable`: Models or dependencies missing

---

### POST /process

**Description**: Upload and process audio file for marker detection.

**Content-Type**: `multipart/form-data`

**Parameters**:
- `file` (required): Audio file (WAV, MP3, M4A, up to 500MB)

**Request Example**:
```bash
curl -X POST \
  -F "file=@session.wav" \
  http://localhost:8765/process
```

**Response**:
```json
{
  "session": "session-4e283a01",
  "input": "session.wav",
  "events": [
    {
      "id": "M_PROSODY_RATE_SLOW",
      "type": "prosody",
      "score": 0.875,
      "ts": 12.5,
      "span": "00:12.50-00:15.20",
      "meta": {
        "wpm": 85,
        "confidence": 0.92
      }
    },
    {
      "id": "SEM_PROJECTION_DEFENSE",
      "type": "text",
      "score": 0.734,
      "ts": 45.2,
      "span": "00:45.20-00:48.10",
      "meta": {
        "text": "Das ist nicht mein Problem",
        "speaker": "client"
      }
    }
  ]
}
```

**Response Fields**:
- `session`: Unique session identifier
- `input`: Original filename
- `events`: Array of detected markers (see Event Schema below)

**Status Codes**:
- `200 OK`: Processing successful
- `400 Bad Request`: Invalid file format or missing file
- `413 Payload Too Large`: File exceeds size limit
- `500 Internal Server Error`: Processing failed
- `504 Gateway Timeout`: Processing exceeded timeout

---

## Event Schema

### Event Object Structure

```json
{
  "id": "string",           // Unique marker identifier
  "type": "string",         // Marker category  
  "score": "number",        // Confidence score (0.0-1.0)
  "ts": "number",           // Timestamp in seconds
  "span": "string",         // Time range in MM:SS.ms format
  "meta": "object"          // Additional metadata
}
```

### Event Types

#### `prosody` - Audio Prosody Markers
Detected from speech patterns, intonation, and timing.

**Common IDs**:
- `M_PROSODY_RATE_SLOW`: Slow speech rate
- `M_PROSODY_RATE_FAST`: Rapid speech
- `M_PROSODY_PITCH_HIGH`: High pitch/stress
- `M_PROSODY_PITCH_LOW`: Low pitch/depression
- `M_PROSODY_HESITATION`: Speech hesitation
- `M_PROSODY_PAUSE_LONG`: Extended pause (>2s)

**Meta Fields**:
- `wpm`: Words per minute
- `pitch_hz`: Average pitch in Hz
- `intensity_db`: Volume in decibels
- `pause_duration`: Pause length in seconds

#### `poseid` - Speaker Identification
Identifies different speakers in multi-speaker sessions.

**Common IDs**:
- `M_POSEID_CLIENT`: Client speaker identified
- `M_POSEID_THERAPIST`: Therapist speaker identified
- `M_POSEID_UNKNOWN`: Unknown speaker

**Meta Fields**:
- `speaker`: Speaker label (`client` | `therapist` | `unknown`)
- `confidence`: Identification confidence (0.0-1.0)
- `embedding_similarity`: Cosine similarity to enrolled profile

#### `text` - Semantic Text Markers
Derived from transcribed content and linguistic patterns.

**Atomic (ATO) Markers**:
- `ATO_SIGH`: Audible sighs
- `ATO_LAUGHTER`: Laughter events  
- `ATO_FILLER`: Filler words ("um", "uh")
- `ATO_HEDGING_CUE`: Hedging language ("maybe", "I think")

**Semantic (SEM) Markers**:
- `SEM_PROJECTION_DEFENSE`: Projection patterns
- `SEM_RESISTANCE_THERAPY`: Therapy resistance
- `SEM_INSIGHT_MOMENT`: Therapeutic insights
- `SEM_EMOTIONAL_BREAKTHROUGH`: Emotional breakthroughs

**Meta Fields**:
- `text`: Relevant text snippet
- `confidence`: Detection confidence
- `context_words`: Surrounding context
- `sentiment_score`: Emotional valence (-1.0 to 1.0)

#### `cluster` - Pattern Clusters
Groups of related markers forming therapeutic patterns.

**Common IDs**:
- `CLU_AVOIDANCE_PATTERN`: Avoidance behaviors
- `CLU_EMOTIONAL_CYCLE`: Recurring emotional patterns
- `CLU_THERAPEUTIC_ALLIANCE`: Alliance strength indicators

**Meta Fields**:
- `pattern_strength`: Pattern confidence (0.0-1.0)
- `constituent_markers`: Component marker IDs
- `duration`: Pattern duration in seconds

#### `meta` - Meta-Level Dynamics
High-level therapeutic process markers.

**Common IDs**:
- `MEMA_BREAKTHROUGH_MOMENT`: Major therapeutic breakthrough
- `MEMA_REGRESSION_PHASE`: Process regression
- `MEMA_INTEGRATION_SUCCESS`: Insight integration

**Meta Fields**:
- `process_stage`: Therapeutic stage indicator
- `significance`: Clinical significance (0.0-1.0)
- `related_themes`: Associated therapeutic themes

---

## Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `CT2_MODELS` | `./models/ct2` | Path to STT models |
| `BUNDLES` | `./bundles/SerapiCore_1.0.yaml` | Active marker bundle |
| `PORT_API` | `8765` | API server port |
| `DEBUG` | `false` | Enable debug logging |
| `MAX_FILE_SIZE` | `500MB` | Maximum upload size |
| `TIMEOUT_SECONDS` | `300` | Processing timeout |

### Scoring Configuration (`scoring/SCR_GLOBAL.json`)

```json
{
  "schema_version": "3.4",
  "weights": {
    "poseid": 1.5,        // Speaker ID importance
    "risk": 1.2,          // Risk marker boost
    "negation": 1.0,      // Negation handling
    "intent": 0.9,        // Intent markers
    "action": 0.8,        // Action markers  
    "prosody": 1.0        // Prosody baseline
  },
  "fusion": {
    "method": "weighted_sum",
    "normalize": true,
    "cap": 1.0
  },
  "thresholds": {
    "emit_event": 0.55    // Minimum score for event emission
  }
}
```

### Bundle Configuration (`bundles/SerapiCore_1.0.yaml`)

```yaml
id: SerapiCore_1.0
version: "3.4"
generated: "2025-09-06"
includes:
  - markers/ATO/ATO_PAUSE_LONG.yaml
  - markers/SEM/SEM_PROJECTION.yaml
  - markers/CLU/CLU_AVOIDANCE.yaml
  # ... 149 additional markers
```

---

## Error Handling

### Error Response Format

```json
{
  "error": "string",      // Error message
  "code": "number",       // Error code
  "details": "object"     // Additional error details
}
```

### Error Codes

| Code | Message | Description |
|------|---------|-------------|
| `12` | Assets fehlen | Missing models or bundle files |
| `20` | Engine nicht verfügbar | Marker engine unavailable |
| `21` | Verarbeitung fehlgeschlagen | Processing failed |
| `504` | Zeitlimit überschritten | Processing timeout exceeded |

### Common Error Scenarios

#### Missing Dependencies
```http
HTTP/1.1 503 Service Unavailable
Content-Type: text/plain

Assets fehlen (models/ct2 oder Bundle).
```

#### Invalid Audio File
```http  
HTTP/1.1 400 Bad Request
Content-Type: text/plain

Unsupported file format. Use WAV, MP3, or M4A.
```

#### Processing Timeout
```http
HTTP/1.1 504 Gateway Timeout
Content-Type: text/plain

Verarbeitung überschritt das Zeitlimit.
```

---

## Rate Limiting

No rate limiting implemented for local deployment. Production deployments should implement appropriate limits based on processing capacity.

**Recommended Limits**:
- Concurrent requests: 1 per instance
- File size: 500MB maximum
- Processing time: 5 minutes maximum

---

## WebSocket API (Future)

*Planned for version 3.5*

### Live Streaming Endpoint

```javascript
// Connect to live processing stream
const ws = new WebSocket('ws://localhost:8765/stream');

// Send audio chunks
ws.send(audioChunk);

// Receive real-time events
ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  console.log('Real-time marker:', data);
};
```

---

## SDK Examples

### Python Client

```python
import requests
import json

class TransRapportClient:
    def __init__(self, base_url="http://localhost:8765"):
        self.base_url = base_url
    
    def health_check(self):
        response = requests.get(f"{self.base_url}/healthz")
        return response.json()
    
    def process_file(self, audio_path):
        with open(audio_path, 'rb') as f:
            files = {'file': f}
            response = requests.post(
                f"{self.base_url}/process", 
                files=files
            )
        return response.json()

# Usage
client = TransRapportClient()
result = client.process_file("session.wav")
print(f"Detected {len(result['events'])} markers")
```

### JavaScript Client

```javascript
class TransRapportClient {
    constructor(baseUrl = 'http://localhost:8765') {
        this.baseUrl = baseUrl;
    }
    
    async healthCheck() {
        const response = await fetch(`${this.baseUrl}/healthz`);
        return await response.json();
    }
    
    async processFile(audioFile) {
        const formData = new FormData();
        formData.append('file', audioFile);
        
        const response = await fetch(`${this.baseUrl}/process`, {
            method: 'POST',
            body: formData
        });
        
        return await response.json();
    }
}

// Usage
const client = new TransRapportClient();
const result = await client.processFile(fileInput.files[0]);
console.log(`Detected ${result.events.length} markers`);
```

### cURL Examples

```bash
# Health check
curl -X GET http://localhost:8765/healthz

# Process audio file
curl -X POST \
  -F "file=@therapy_session.wav" \
  -H "Accept: application/json" \
  http://localhost:8765/process

# Process with custom timeout
curl -X POST \
  -F "file=@long_session.wav" \
  -H "X-Timeout: 600" \
  http://localhost:8765/process
```

---

## Performance Considerations

### Processing Time Estimates

| Audio Length | Processing Time | Memory Usage |
|--------------|-----------------|--------------|
| 5 minutes | 30-60 seconds | 1-2 GB |
| 30 minutes | 3-8 minutes | 2-4 GB |
| 60 minutes | 8-15 minutes | 4-8 GB |
| 120 minutes | 15-30 minutes | 6-12 GB |

### Optimization Tips

1. **Audio Quality**: 16kHz mono WAV files process fastest
2. **File Size**: Compress large files before upload  
3. **Concurrent Processing**: Only one session per instance
4. **Memory**: Ensure sufficient RAM for longer sessions
5. **Storage**: Keep 2x file size as free disk space

### System Requirements

**Minimum**:
- CPU: 4-core 2.4GHz
- RAM: 8GB
- Storage: 10GB free space
- OS: Windows 10, macOS 10.15, Ubuntu 18.04

**Recommended**:
- CPU: 8-core 3.0GHz  
- RAM: 16GB
- Storage: SSD with 20GB free space
- OS: Latest versions

---

## Security

### Data Protection

- **Offline Processing**: No data leaves local machine
- **Encryption**: All stored data encrypted at rest
- **Temporary Files**: Cleaned up after processing
- **Access Control**: Local filesystem permissions only

### Privacy Compliance

- **GDPR**: Compliant for EU therapy practices
- **HIPAA**: Suitable for US healthcare with proper setup
- **Local Laws**: Check regional data protection requirements
- **Client Consent**: Always obtain explicit recording consent

### Security Best Practices

1. **Network Isolation**: Run on isolated network segment
2. **Access Logging**: Monitor API access patterns  
3. **File Validation**: Validate all uploaded content
4. **Resource Limits**: Implement processing quotas
5. **Regular Updates**: Keep system components current

---

## Monitoring and Logging

### Log Levels

| Level | Description | Location |
|-------|-------------|----------|
| `DEBUG` | Detailed processing info | `logs/debug.log` |
| `INFO` | General operation status | `logs/info.log` |
| `WARN` | Non-critical issues | `logs/warn.log` |
| `ERROR` | Processing failures | `logs/error.log` |

### Metrics Collection

```json
{
  "timestamp": "2025-09-06T14:30:00Z",
  "session_id": "session-abc123",
  "processing_time": 45.2,
  "audio_length": 1800,
  "events_detected": 23,
  "file_size_mb": 85.4,
  "success": true
}
```

### Health Monitoring

Monitor these endpoints for system health:

- `GET /healthz`: Basic system status
- `GET /metrics`: Processing statistics (if enabled)
- Log file sizes and error rates
- System resource utilization

---

## Version History

### Version 3.4 (September 2025)
- LEAN.DEEP 3.4 marker schema
- Unified engine adapter
- SID to poseid conversion
- Bundle generation automation
- Registry system overhaul

### Version 3.3 (August 2025)  
- Multi-speaker detection
- Improved prosody analysis
- Real-time processing optimization
- Enhanced error handling

### Version 3.2 (July 2025)
- Initial FastAPI implementation
- Basic marker detection
- File upload support
- Offline operation

---

## Support and Development

### Getting Help

- **Documentation**: `/docs/` directory
- **API Reference**: This document
- **Community**: GitHub Discussions
- **Email**: support@transrapport.de

### Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature/api-enhancement`
3. Commit changes: `git commit -m "Add new endpoint"`
4. Push branch: `git push origin feature/api-enhancement`
5. Create Pull Request

### License

**CC BY-NC-SA 4.0** - Non-commercial use with attribution required.

For commercial licensing, contact: licensing@transrapport.de

---

*API Documentation Version 3.4 - Last Updated: September 6, 2025*
