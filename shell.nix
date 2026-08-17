{
  pkgs ? import <nixpkgs> { },
}:

with pkgs;
mkShell {
  name = "astyle-wheel";
  env = {
    CMAKE_GENERATOR = "Ninja";
  };
  buildInputs = [
    git
    uv
    ninja

    (python3.withPackages (
      p: with p; [
        pytest
        scikit-build-core

        cython
        autopxd2
      ]
    ))
  ];
}
