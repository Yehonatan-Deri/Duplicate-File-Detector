# Duplicate File Detector

A Python-based application for identifying and managing duplicate files in a specified directory.

## Features

- Graphical user interface for easy interaction
- Support for multiple file types (images, documents, etc.)
- Image preview capability for visual comparison
- Customizable file extension filters
- Duplicate detection using file hash comparison
- Batch delete/move operations for managing duplicates

## Technical Architecture

### Components

1. **GUI Layer (PyQt/tkinter)**
   - Main window management
   - Settings panel
   - Results display
   - File preview
   - Progress indication

2. **Controller**
   - Orchestrates communication between GUI and core components
   - Manages scan operations
   - Handles user actions
   - Updates UI state

3. **File Scanner**
   - Recursive directory traversal
   - File filtering by extension
   - Progress tracking
   - Memory-efficient file handling

4. **Image Handler**
   - Image loading and thumbnail generation
   - Format validation
   - Memory-efficient preview caching

5. **File Hash Calculator**
   - Efficient file hashing (SHA-256)
   - Partial content hashing for large files
   - Multi-threaded processing

### Data Flow

1. User initiates scan:
   - Selects directory
   - Configures file extensions
   - Starts scan operation

2. Scanning process:
   - Recursive directory traversal
   - File filtering
   - Hash calculation
   - Progress updates

3. Results processing:
   - Group duplicate files
   - Generate previews
   - Update UI
   - Cache results

4. User actions:
   - View file details
   - Preview content
   - Select files for action
   - Execute batch operations

## Implementation Plan

### Phase 1: Core Framework
- [ ] Project setup and structure
- [ ] Basic GUI implementation
- [ ] File system operations
- [ ] Hash calculation logic

### Phase 2: Features
- [ ] File scanning and comparison
- [ ] Image preview functionality
- [ ] Results display
- [ ] File operations (delete/move)

### Phase 3: Optimization
- [ ] Performance improvements
- [ ] Memory optimization
- [ ] Multi-threading
- [ ] Progress tracking

### Phase 4: Polish
- [ ] User settings
- [ ] Error handling
- [ ] UI improvements
- [ ] Testing and bug fixes

## File Structure

```
duplicate-file-detector/
├── src/
│   ├── gui/
│   │   ├── __init__.py
│   │   ├── main_window.py
│   │   ├── settings_panel.py
│   │   └── results_view.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── scanner.py
│   │   ├── hasher.py
│   │   └── image_handler.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── file_ops.py
│   └── main.py
├── tests/
│   ├── test_scanner.py
│   ├── test_hasher.py
│   └── test_image_handler.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python src/main.py
   ```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License - See LICENSE file for details
