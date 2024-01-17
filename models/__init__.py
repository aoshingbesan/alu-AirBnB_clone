#!/usr/bin/python3

'''Creates a unique 'FileStorage' instance for our application
'''
import models.engine.file_storage as file_storage

storage = file_storage.FileStorage()
storage.reload()
