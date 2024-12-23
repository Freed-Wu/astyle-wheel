{
  pkgs ? import <nixpkgs> { },
}:

with pkgs;
mkShell {
  name = "astyle-wheel";
  buildInputs = [
    git

    stdenv.cc

    (python3.withPackages (
      p: with p; [
        uv
        pytest
        scikit-build-core

        cython
        autopxd2
      ]
    ))
  ];
  shellHook = ''
    export CMAKE_GENERATOR=Ninja
  '';
}
