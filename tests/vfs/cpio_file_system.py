#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Tests for the file system implementation using the CPIOArchiveFile."""

from __future__ import unicode_literals

import unittest

from dfvfs.path import cpio_path_spec
from dfvfs.path import os_path_spec
from dfvfs.resolver import context
from dfvfs.vfs import cpio_file_system

from tests import test_lib as shared_test_lib


@shared_test_lib.skipUnlessHasTestFile(['syslog.bin.cpio'])
class CPIOFileSystemTest(shared_test_lib.BaseTestCase):
  """The unit test for the CPIO file system object."""

  def setUp(self):
    """Sets up the needed objects used throughout the test."""
    self._resolver_context = context.Context()
    test_file = self._GetTestFilePath(['syslog.bin.cpio'])
    self._os_path_spec = os_path_spec.OSPathSpec(location=test_file)
    self._cpio_path_spec = cpio_path_spec.CPIOPathSpec(
        location='/syslog', parent=self._os_path_spec)

  def testOpenAndClose(self):
    """Test the open and close functionality."""
    file_system = cpio_file_system.CPIOFileSystem(self._resolver_context)
    self.assertIsNotNone(file_system)

    file_system.Open(self._cpio_path_spec)

    file_system.Close()

  def testFileEntryExistsByPathSpec(self):
    """Test the file entry exists by path specification functionality."""
    file_system = cpio_file_system.CPIOFileSystem(self._resolver_context)
    self.assertIsNotNone(file_system)

    file_system.Open(self._cpio_path_spec)

    path_spec = cpio_path_spec.CPIOPathSpec(
        location='/syslog', parent=self._os_path_spec)
    self.assertTrue(file_system.FileEntryExistsByPathSpec(path_spec))

    path_spec = cpio_path_spec.CPIOPathSpec(
        location='/bogus', parent=self._os_path_spec)
    self.assertFalse(file_system.FileEntryExistsByPathSpec(path_spec))

    file_system.Close()

  def testGetFileEntryByPathSpec(self):
    """Tests the GetFileEntryByPathSpec function."""
    file_system = cpio_file_system.CPIOFileSystem(self._resolver_context)
    self.assertIsNotNone(file_system)

    file_system.Open(self._cpio_path_spec)

    path_spec = cpio_path_spec.CPIOPathSpec(
        location='/syslog', parent=self._os_path_spec)
    file_entry = file_system.GetFileEntryByPathSpec(path_spec)

    self.assertIsNotNone(file_entry)
    self.assertEqual(file_entry.name, 'syslog')

    path_spec = cpio_path_spec.CPIOPathSpec(
        location='/bogus', parent=self._os_path_spec)
    file_entry = file_system.GetFileEntryByPathSpec(path_spec)

    self.assertIsNone(file_entry)

    file_system.Close()

  def testGetRootFileEntry(self):
    """Test the get root file entry functionality."""
    file_system = cpio_file_system.CPIOFileSystem(self._resolver_context)
    self.assertIsNotNone(file_system)

    file_system.Open(self._cpio_path_spec)

    file_entry = file_system.GetRootFileEntry()

    self.assertIsNotNone(file_entry)
    self.assertEqual(file_entry.name, '')

    file_system.Close()

  # TODO: add tests for GetCPIOArchiveFileEntryByPathSpec function.


if __name__ == '__main__':
  unittest.main()
