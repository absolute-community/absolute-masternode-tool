## Building the Absolute Masternode Tool executable on macOS

You can build Absolute Masternode Tool for macOS by opening the Terminal app and running the following commands:

* Install *Homebrew*:

  ```
  /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
  ```

  Installation takes about 5 minutes to complete.

* Install *Python 3*:

  ```
  brew install python3
  ```

* After the installation process completes, make sure that the Python version installed is 3.6 or newer. DMT won't compile on older versions of Python, or even older versions of Python 3:

  ```
  python3 --version
  ```

  You should see a response similar to the following:

  `Python 3.6.4`

* Install *virtualenv*:

  ```
  pip3 install virtualenv
  ```

* Create a Python virtual environment for DMT:

  ```
  cd ~
  mkdir projects
  mkdir projects/virtualenvs
  cd projects/virtualenvs
  virtualenv -p python3 dmt
  ```

* Activate the new virtual environment:

  ```
  source dmt/bin/activate
  ```

* Download the DMT source from GitHub:

  ```
  cd ~/projects
  git clone https://github.com/absolute-community/absolute-masternode-tool
  ```

* Install the DMT Python requirements:

  ```
  cd absolute-masternode-tool
  pip install -r requirements.txt
  ```

* Build the DMT executable:

  ```
  pyinstaller --distpath=../dist/mac --workpath=../build/mac absolute_masternode_tool.spec
  ```


Once the build has completed successfully, a compressed macOS executable file will be created in the ***~/projects/dist/all*** directory. An uncompressed app package (*AbsoluteMasternodeTool.app*) can be found in the ***~/projects/dist/mac*** directory.