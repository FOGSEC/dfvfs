# -*- coding: utf-8 -*-
"""The encoded stream path specification resolver helper implementation."""

from __future__ import unicode_literals

# This is necessary to prevent a circular import.
import dfvfs.file_io.encoded_stream_io
import dfvfs.vfs.encoded_stream_file_system

from dfvfs.lib import definitions
from dfvfs.resolver import resolver
from dfvfs.resolver import resolver_helper


class EncodedStreamResolverHelper(resolver_helper.ResolverHelper):
  """Encoded stream resolver helper."""

  TYPE_INDICATOR = definitions.TYPE_INDICATOR_ENCODED_STREAM

  def NewFileObject(self, resolver_context):
    """Creates a new file-like object.

    Args:
      resolver_context (Context): resolver context.

    Returns:
      FileIO: file-like object.
    """
    return dfvfs.file_io.encoded_stream_io.EncodedStream(resolver_context)

  def NewFileSystem(self, resolver_context):
    """Creates a new file system object.

    Args:
      resolver_context (Context): resolver context.

    Returns:
      FileSystem: file system.
    """
    return dfvfs.vfs.encoded_stream_file_system.EncodedStreamFileSystem(
        resolver_context)


resolver.Resolver.RegisterHelper(EncodedStreamResolverHelper())
