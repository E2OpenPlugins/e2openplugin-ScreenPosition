from distutils.core import setup, Extension

pkg = 'Extensions.ScreenPosition'
setup(name='enigma2-plugin-extensions-screenposition',
       version='0.1',
       description='ScreenPosition',
       packages=[pkg],
       package_dir={pkg: 'plugin'}
      )
