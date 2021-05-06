with import <nixpkgs> {};
stdenv.mkDerivation {
  name = "bruuh";
  buildInputs = [ python38 pipenv ];
  }
