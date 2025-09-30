#!/bin/bash

# Arachnida Test Runner
# Simple script to run all tests with colored output

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${BLUE}╔══════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║         ARACHNIDA TEST SUITE             ║${NC}"
echo -e "${BLUE}╚══════════════════════════════════════════╝${NC}"
echo ""

# Check if we're in the right directory
if [[ ! -f "spider.py" ]] || [[ ! -f "scorpion.py" ]]; then
    echo -e "${RED}Error: Please run this script from the arachnida project root${NC}"
    echo -e "${YELLOW}Expected files: spider.py, scorpion.py${NC}"
    exit 1
fi

# Check Python and dependencies
echo -e "${CYAN}Checking dependencies...${NC}"

python3 -c "import requests, bs4, PIL" 2>/dev/null
if [[ $? -eq 0 ]]; then
    echo -e "${GREEN}✅ All dependencies available${NC}"
else
    echo -e "${RED}❌ Missing dependencies${NC}"
    echo -e "${YELLOW}Install with: pip install requests beautifulsoup4 pillow${NC}"
    exit 1
fi

echo ""

# Run the test suite
echo -e "${PURPLE}Running test suite...${NC}"
echo ""

python3 -m pytest tests/test_arachnida.py -v 2>/dev/null || \
python3 tests/test_arachnida.py

exit_code=$?

echo ""

# Results summary
if [[ $exit_code -eq 0 ]]; then
    echo -e "${GREEN}🎉 All tests passed!${NC}"
    echo -e "${GREEN}✅ Spider functionality working${NC}"
    echo -e "${GREEN}✅ Scorpion functionality working${NC}"
    echo -e "${GREEN}✅ Error handling robust${NC}"
    echo -e "${GREEN}✅ Dependencies satisfied${NC}"
else
    echo -e "${RED}❌ Some tests failed${NC}"
    echo -e "${YELLOW}Check the output above for details${NC}"
fi

echo ""
echo -e "${BLUE}Test suite complete!${NC}"

exit $exit_code