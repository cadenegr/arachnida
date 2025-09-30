# Arachnida Test Suite Documentation

## Overview

Simple but comprehensive test suite for the Arachnida web scraping and image metadata analysis tools.

## Test Categories

### 🕷️ **Spider Tests** (4 tests)
- **Help functionality** - Validates CLI help system
- **Invalid URL handling** - Tests graceful error handling
- **Directory creation** - Ensures proper file operations
- **Recursive functionality** - Validates depth-controlled crawling

### 🦂 **Scorpion Tests** (4 tests)  
- **Help functionality** - Validates CLI help system
- **Nonexistent file handling** - Tests error handling
- **Valid image processing** - Tests metadata extraction
- **Directory processing** - Tests batch operations

### 🔧 **Dependency Tests** (3 tests)
- **Requests library** - Web scraping capability
- **BeautifulSoup** - HTML parsing functionality
- **PIL/Pillow** - Image processing capability

### 🔄 **Integration Tests** (1 test)
- **Workflow compatibility** - Tests spider→scorpion pipeline

## Running Tests

### Quick Test Run
```bash
./tests/run_tests.sh
```

### Direct Python Execution
```bash
python3 tests/test_arachnida.py
```

### Individual Test Categories
```bash
# Test only spider functionality
python3 -m unittest tests.test_arachnida.TestSpider

# Test only scorpion functionality  
python3 -m unittest tests.test_arachnida.TestScorpion

# Test only dependencies
python3 -m unittest tests.test_arachnida.TestDependencies
```

## Test Results Interpretation

### ✅ **Success Indicators**
- All dependency tests pass
- Help systems work correctly
- Error handling is graceful
- File operations succeed
- Integration workflow functions

### ⚠️ **Common Skip Conditions**
- PIL test skipped if Pillow not available
- Image processing tests skipped if test images can't be created

### ❌ **Failure Scenarios**
- Missing dependencies (requests, beautifulsoup4, pillow)
- File permission issues
- Network connectivity problems (for integration tests)

## Test Coverage

### **Functional Coverage**
- ✅ CLI argument parsing and help systems
- ✅ Error handling for invalid inputs
- ✅ File and directory operations
- ✅ Network request handling
- ✅ Metadata extraction capabilities

### **Quality Assurance**
- ✅ Dependency validation
- ✅ Graceful error handling
- ✅ Integration compatibility
- ✅ Cross-platform file operations

## Extending the Test Suite

### Adding New Tests
1. Add test methods to appropriate TestCase class
2. Use descriptive test names: `test_feature_description`
3. Include docstrings explaining test purpose
4. Follow setUp/tearDown pattern for test isolation

### Test Structure Template
```python
def test_new_functionality(self):
    """Test description"""
    # Arrange - set up test conditions
    
    # Act - execute the functionality
    
    # Assert - verify the results
    self.assertEqual(expected, actual)
```

## Performance Considerations

- **Fast execution** - Most tests complete in under 5 seconds
- **Isolated testing** - Each test uses temporary directories
- **Network minimal** - Limited external network calls
- **Memory efficient** - Proper cleanup after each test

## Integration with Development Workflow

### Pre-commit Testing
```bash
# Run before committing changes
./tests/run_tests.sh
```

### CI/CD Integration
```bash
# For automated testing pipelines
python3 tests/test_arachnida.py
exit_code=$?
if [[ $exit_code -eq 0 ]]; then
    echo "Tests passed - ready for deployment"
else
    echo "Tests failed - fix before deploying"
    exit $exit_code
fi
```

This test suite provides confidence in the reliability and robustness of both spider and scorpion tools while maintaining simplicity and fast execution.