from conans import ConanFile, CMake, tools


class SignalsConan(ConanFile):
    name = "signals"
    version = "0.0.1"
    license = "MIT"
    url = "https://github.com/winternet/conan-signals"
    description = "vdksoft-signals is a thread and typesafe signal-slot system"
    topics = ("C++17", "thread-safe", "typesafe", "signal-slot")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def source(self):
        self.run("git clone https://github.com/winternet/signals.git")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="signals")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="signals/include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["signals"]

