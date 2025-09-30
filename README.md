# 🕷️ Arachnida - Advanced Web Image Scraping & Metadata Analysis Suite

A sophisticated **dual-component image processing toolkit** featuring intelligent web scraping with recursive crawling capabilities and comprehensive EXIF metadata extraction. Built with robust error handling, security-conscious design, and professional CLI interfaces.

## 🎯 Project Overview

**Arachnida** combines two powerful tools for image acquisition and analysis:

- **🕷️ Spider**: Intelligent web crawler with recursive image downloading
- **🦂 Scorpion**: Advanced EXIF and metadata extraction engine

This project demonstrates advanced **web scraping techniques**, **image processing algorithms**, and **robust system design** with comprehensive error handling and security considerations.

## 🚀 Key Technical Features

### **🧠 Intelligent Web Crawling**
- **Recursive depth-controlled scraping** with configurable limits
- **Smart URL resolution** handling relative, absolute, and protocol-relative URLs
- **Duplicate prevention system** using visited URL tracking
- **Browser-mimicking headers** for reliable access to protected content
- **Robust error recovery** with graceful failure handling

### **🔍 Advanced Metadata Processing**
- **Comprehensive EXIF extraction** using PIL/Pillow integration
- **Multi-format support** (.jpg, .jpeg, .png, .gif, .bmp)
- **File system metadata** including creation dates and attributes
- **Batch processing** for directories and individual files
- **Structured output formatting** for easy analysis

### **🛡️ Security & Reliability**
- **Safe downloading practices** with proper content validation
- **Request rate limiting** through intelligent crawling
- **Path sanitization** preventing directory traversal attacks
- **Memory-efficient processing** for large-scale operations

## 📦 Installation & Setup

### Option 1: Package Installation (Recommended)
```bash
# Clone the repository
git clone https://github.com/cadenegr/arachnida.git
cd arachnida

# Install dependencies
pip install -r requirements.txt

# Install as a Python package
pip install .

# Now use anywhere with:
spider --help
scorpion --help
```

### Option 2: Development Mode
```bash
# Clone the repository
git clone https://github.com/cadenegr/arachnida.git
cd arachnida

# Install dependencies
pip install -r requirements.txt

# Install in development mode (editable)
pip install -e .

# Or run directly:
python spider.py --help
python scorpion.py --help
```

### Option 3: Direct Execution
```bash
# Clone the repository
git clone https://github.com/cadenegr/arachnida.git
cd arachnida

# Install dependencies manually
pip install requests beautifulsoup4 pillow

# Make scripts executable and run
chmod +x spider.py scorpion.py
./spider.py --help
./scorpion.py --help
```

## 🕷️ Spider - Web Image Crawler

**Recursively downloads images from websites with intelligent crawling algorithms.**

### Usage
```bash
# Basic image download
python spider.py https://example.com

# Recursive download with custom depth
python spider.py -r -l 3 https://example.com

# Custom download directory
python spider.py -r -p ./images https://example.com

# Full recursive crawl (default depth: 5)
python spider.py -r https://example.com

# After package installation:
spider -r -l 2 https://example.com
```

### Advanced Options
```bash
python spider.py [-r] [-l DEPTH] [-p PATH] URL

# Or after installation:
spider [-r] [-l DEPTH] [-p PATH] URL

Options:
  -r          Enable recursive crawling mode
  -l DEPTH    Maximum crawl depth (default: 5)
  -p PATH     Download directory (default: ./spider)
  URL         Target website URL
```

### Technical Implementation Highlights

#### Smart URL Resolution Algorithm
```python
# Handles multiple URL formats intelligently
if next_url.startswith("//"):
    next_url = "https:" + next_url          # Protocol-relative
elif next_url.startswith("/"):
    next_url = urljoin(url, next_url)       # Site-relative
elif not next_url.startswith(("http:", "https:")):
    continue                                # Skip invalid URLs
```

#### Duplicate Prevention System
- **Visited URL tracking** prevents infinite crawling loops
- **Depth-limited recursion** ensures controlled exploration
- **Memory-efficient design** for large-scale operations

#### Browser-Like Request Headers
```python
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:118.0) Gecko/20100101 Firefox/118.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://www.google.com/",
}
```

## 🦂 Scorpion - EXIF Metadata Extractor

**Comprehensive image metadata analysis with EXIF parsing and file system information.**

### Usage
```bash
# Single image analysis
python scorpion.py image.jpg

# Multiple images
python scorpion.py img1.jpg img2.png img3.gif

# Directory processing
python scorpion.py ./images/

# Mixed input types
python scorpion.py image.jpg ./folder/ another.png

# After package installation:
scorpion image.jpg ./photos/
```

### Metadata Extraction Capabilities

#### EXIF Data Analysis
- **Camera information** (make, model, lens details)
- **Shooting parameters** (ISO, aperture, shutter speed)
- **GPS coordinates** (if available)
- **Creation timestamps** and modification dates
- **Image dimensions** and color profiles

#### File System Metadata
- **Creation timestamps** with precise formatting
- **File size** and storage information
- **Path normalization** for cross-platform compatibility

### Example Output
```
Metadata for ./images/photo.jpg:
EXIF Data:
DateTime: 2024:09:30 14:23:17
Make: Canon
Model: EOS R5
FNumber: (28, 10)
ExposureTime: (1, 125)
ISOSpeedRatings: 400
FocalLength: (85, 1)

File Metadata:
Creation Date: 2024-09-30 14:23:17
```

## 🏗️ Architecture & Design

### Component Interaction
```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐
│   Spider    │───▶│  Downloaded  │───▶│  Scorpion   │
│ (Crawler)   │    │   Images     │    │ (Analyzer)  │
└─────────────┘    └──────────────┘    └─────────────┘
      │                    │                   │
      ▼                    ▼                   ▼
┌─────────────┐    ┌──────────────┐    ┌─────────────┐
│ Web Content │    │ File Storage │    │  Metadata   │
│  Analysis   │    │ Management   │    │ Extraction  │
└─────────────┘    └──────────────┘    └─────────────┘
```

### Core Algorithms

#### Recursive Crawling Strategy
1. **URL Validation** - Verify and normalize target URLs
2. **Content Parsing** - Extract images and links using BeautifulSoup
3. **Depth Management** - Control recursion with configurable limits
4. **Duplicate Prevention** - Track visited URLs to prevent loops
5. **Error Recovery** - Graceful handling of network and parsing errors

#### Metadata Extraction Pipeline
1. **Format Detection** - Identify supported image formats
2. **EXIF Parsing** - Extract technical metadata using PIL
3. **File Analysis** - Gather filesystem information
4. **Data Formatting** - Structure output for readability
5. **Batch Processing** - Handle multiple files efficiently

## 🔧 Technical Specifications

### Supported Image Formats
- **JPEG/JPG** - Full EXIF support including GPS data
- **PNG** - Metadata and creation information
- **GIF** - Basic metadata extraction
- **BMP** - File system information

### Performance Characteristics
- **Memory Efficient** - Streaming download and processing
- **Network Optimized** - Intelligent request handling
- **Scalable Design** - Handles large websites and image collections
- **Error Resilient** - Continues operation despite individual failures

### Security Features
- **Safe Path Handling** - Prevents directory traversal
- **Content Validation** - Verifies downloaded content
- **Request Headers** - Mimics legitimate browser behavior
- **Error Isolation** - Individual failures don't crash the system

## 💡 Use Cases & Applications

### Digital Forensics
- **Website archiving** for evidence collection
- **Image metadata analysis** for investigation purposes
- **Bulk processing** of evidence collections

### Content Management
- **Asset discovery** and cataloging
- **Metadata extraction** for organization systems
- **Bulk download** for backup and analysis

### Research & Analysis
- **Web content study** and statistical analysis
- **Image collection** for machine learning datasets
- **Metadata research** for digital humanities projects

## 🧪 Testing

### Quick Test Validation
```bash
# Run the comprehensive test suite
./tests/run_tests.sh

# Or run tests directly with Python
python tests/test_arachnida.py

# Run specific test categories
python -m unittest tests.test_arachnida.TestSpider
python -m unittest tests.test_arachnida.TestScorpion
```

### Test Coverage
- ✅ **Spider functionality** - Web crawling and file operations
- ✅ **Scorpion capabilities** - Metadata extraction and processing  
- ✅ **Dependency validation** - All required packages available
- ✅ **Integration workflow** - End-to-end pipeline testing
- ✅ **Error handling** - Graceful failure management

## 🎯 Advanced Features

### Error Handling & Resilience
```python
try:
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    # Process successful response
except requests.RequestException as e:
    print(f"Failed to fetch {url}: {e}")
    # Continue with next URL
```

### Smart Content Detection
- **HTML parsing** with BeautifulSoup for robust extraction
- **Image validation** before download attempts
- **Content-type verification** for security

### Configurable Behavior
- **Flexible depth control** for crawling scope
- **Custom output directories** for organization
- **Extensible format support** for future enhancements

## 🏆 Why This Implementation Stands Out

1. **🧠 Algorithmic Sophistication**: Intelligent crawling with depth control and duplicate prevention
2. **🛡️ Security Conscious**: Safe downloading practices and proper error handling
3. **⚡ Performance Optimized**: Memory-efficient design for large-scale operations
4. **🔧 Professional Architecture**: Clean separation of concerns and modular design
5. **📊 Comprehensive Analysis**: Deep metadata extraction beyond basic file information

## 👨‍💻 Technical Skills Demonstrated

- **Web Scraping Expertise** - Advanced crawling algorithms and content extraction
- **Image Processing** - EXIF parsing and metadata analysis with PIL
- **Network Programming** - HTTP request handling and error recovery
- **CLI Design** - Professional argument parsing and user interface
- **Error Handling** - Robust exception management and graceful failures
- **Security Awareness** - Safe practices for web interaction and file handling

## 🔮 Future Enhancements

- **Multi-threading** for parallel download processing
- **Database integration** for metadata storage and querying
- **Web interface** for remote operation and monitoring
- **Advanced filtering** with regex patterns and content rules
- **Cloud storage** integration for distributed operations

---

*This project showcases advanced Python programming skills with focus on web technologies, image processing, and robust system design. The combination of intelligent crawling algorithms and comprehensive metadata analysis demonstrates proficiency in both network programming and data extraction techniques.*
