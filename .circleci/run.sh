
#!/bin/bash

set -e
set -x

conan remote add ${CONAN_REMOTE} ${CONAN_REPO}
conan user -p ${CONAN_API_KEY} -r ${CONAN_REMOTE} ${CONAN_USER}
conan create . signals/0.0.1@winternet/testing
conan upload signals/0.0.1@winternet/testing -r ${CONAN_REMOTE}
