{
  pkgs ? import <nixpkgs> { },
}:

with pkgs;
mkShell {
  name = "astyle-wheel";
  buildInputs = [
    cmake
    ninja

    git

    (python3.withPackages (
      p: with p; [
        build
        pytest

        cython
        autopxd2
      ]
    ))
  ];
  shellHook = ''
    export CMAKE_GENERATOR=Ninja
  '';
}
