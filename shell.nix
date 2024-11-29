{
  pkgs ? import <nixpkgs> { },
}:

with pkgs;
mkShell {
  name = "astyle-wheel";
  buildInputs = [
    cmake
    ninja
    (python3.withPackages (
      p: with p; [
        cython
      ]
    ))
  ];
  shellHook = ''
    export CMAKE_GENERATOR=Ninja
  '';
}
