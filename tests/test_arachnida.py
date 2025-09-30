#!/usr/bin/env python3
"""
Simple Test Suite for Arachnida Project
Tests core functionality of spider and scorpion tools
"""

import unittest
import os
import sys
import tempfile
import shutil
from unittest.mock import patch, MagicMock
import subprocess

# Add project root to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestSpider(unittest.TestCase):
    """Test cases for spider.py functionality"""
    
    def setUp(self):
        """Set up test environment"""
        self.test_dir = tempfile.mkdtemp()
        self.spider_path = os.path.join(os.path.dirname(__file__), '..', 'spider.py')
    
    def tearDown(self):
        """Clean up test environment"""
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def test_spider_help(self):
        """Test spider help functionality"""
        result = subprocess.run([
            'python3', self.spider_path, '--help'
        ], capture_output=True, text=True)
        
        self.assertEqual(result.returncode, 0)
        self.assertIn('Spider - Download images script', result.stdout)
        self.assertIn('url', result.stdout)
        self.assertIn('-r', result.stdout)
    
    def test_spider_invalid_url(self):
        """Test spider behavior with invalid URL"""
        result = subprocess.run([
            'python3', self.spider_path, 'invalid://url'
        ], capture_output=True, text=True, cwd=self.test_dir)
        
        self.assertEqual(result.returncode, 0)  # Should handle gracefully
        self.assertIn('Failed to fetch', result.stdout)
    
    def test_spider_directory_creation(self):
        """Test that spider creates download directory"""
        test_path = os.path.join(self.test_dir, 'downloads')
        
        # Run spider with a simple URL (will fail but should create directory)
        subprocess.run([
            'python3', self.spider_path, '-p', test_path, 'https://example.com'
        ], capture_output=True, text=True)
        
        self.assertTrue(os.path.exists(test_path))
    
    def test_spider_recursive_flag(self):
        """Test spider with recursive flag"""
        result = subprocess.run([
            'python3', self.spider_path, '-r', '-l', '1', 'https://example.com'
        ], capture_output=True, text=True, cwd=self.test_dir)
        
        self.assertEqual(result.returncode, 0)
        # Should process without errors
        self.assertNotIn('Traceback', result.stderr)


class TestScorpion(unittest.TestCase):
    """Test cases for scorpion.py functionality"""
    
    def setUp(self):
        """Set up test environment"""
        self.test_dir = tempfile.mkdtemp()
        self.scorpion_path = os.path.join(os.path.dirname(__file__), '..', 'scorpion.py')
        
        # Create a test image
        try:
            from PIL import Image
            self.test_image = os.path.join(self.test_dir, 'test.jpg')
            img = Image.new('RGB', (100, 100), color='red')
            img.save(self.test_image)
        except ImportError:
            self.test_image = None
    
    def tearDown(self):
        """Clean up test environment"""
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def test_scorpion_help(self):
        """Test scorpion help functionality"""
        result = subprocess.run([
            'python3', self.scorpion_path, '--help'
        ], capture_output=True, text=True)
        
        self.assertEqual(result.returncode, 0)
        self.assertIn('Scorpion - EXIF and Metadata Viewer', result.stdout)
        self.assertIn('inputs', result.stdout)
    
    def test_scorpion_nonexistent_file(self):
        """Test scorpion behavior with nonexistent file"""
        result = subprocess.run([
            'python3', self.scorpion_path, 'nonexistent.jpg'
        ], capture_output=True, text=True)
        
        self.assertEqual(result.returncode, 0)  # Should handle gracefully
        self.assertIn('Invalid input', result.stdout)
    
    @unittest.skipIf(not os.environ.get('PIL_AVAILABLE'), "PIL not available")
    def test_scorpion_valid_image(self):
        """Test scorpion with valid image file"""
        if not self.test_image:
            self.skipTest("Could not create test image")
        
        result = subprocess.run([
            'python3', self.scorpion_path, self.test_image
        ], capture_output=True, text=True)
        
        self.assertEqual(result.returncode, 0)
        self.assertIn('Metadata for', result.stdout)
        self.assertIn('Creation Date', result.stdout)
    
    def test_scorpion_directory_processing(self):
        """Test scorpion with directory input"""
        if not self.test_image:
            self.skipTest("Could not create test image")
        
        result = subprocess.run([
            'python3', self.scorpion_path, self.test_dir
        ], capture_output=True, text=True)
        
        self.assertEqual(result.returncode, 0)
        self.assertIn('Processing images in folder', result.stdout)


class TestDependencies(unittest.TestCase):
    """Test that all required dependencies are available"""
    
    def test_requests_available(self):
        """Test that requests library is available"""
        try:
            import requests
            self.assertTrue(True)
        except ImportError:
            self.fail("requests library not available")
    
    def test_beautifulsoup_available(self):
        """Test that BeautifulSoup is available"""
        try:
            from bs4 import BeautifulSoup
            self.assertTrue(True)
        except ImportError:
            self.fail("BeautifulSoup library not available")
    
    def test_pil_available(self):
        """Test that PIL/Pillow is available"""
        try:
            from PIL import Image
            os.environ['PIL_AVAILABLE'] = '1'
            self.assertTrue(True)
        except ImportError:
            self.fail("PIL/Pillow library not available")


class TestIntegration(unittest.TestCase):
    """Integration tests for the complete workflow"""
    
    def setUp(self):
        """Set up integration test environment"""
        self.test_dir = tempfile.mkdtemp()
        self.spider_path = os.path.join(os.path.dirname(__file__), '..', 'spider.py')
        self.scorpion_path = os.path.join(os.path.dirname(__file__), '..', 'scorpion.py')
    
    def tearDown(self):
        """Clean up integration test environment"""
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def test_workflow_compatibility(self):
        """Test that spider output can be processed by scorpion"""
        download_dir = os.path.join(self.test_dir, 'downloads')
        
        # Run spider (will create directory even if no images found)
        spider_result = subprocess.run([
            'python3', self.spider_path, '-p', download_dir, 'https://example.com'
        ], capture_output=True, text=True)
        
        self.assertEqual(spider_result.returncode, 0)
        self.assertTrue(os.path.exists(download_dir))
        
        # Run scorpion on the download directory
        scorpion_result = subprocess.run([
            'python3', self.scorpion_path, download_dir
        ], capture_output=True, text=True)
        
        self.assertEqual(scorpion_result.returncode, 0)


if __name__ == '__main__':
    # Run all tests
    unittest.main(verbosity=2)