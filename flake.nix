{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/release-22.11";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = inputs:
    let
      overlay = final: prev: { };
      perSystem = system:
        let
          pkgs = import inputs.nixpkgs { inherit system; overlays = [ overlay ]; };

          my-python = pkgs.python3.withPackages (p: with p; [
            matplotlib
            numpy
            scipy
            black
            qutip
          ]);

        in
        {
          devShell = pkgs.mkShell {
            buildInputs = with pkgs; [
              my-python

              entr
              fd
              feh
              gnumake
            ];
          };
        };
    in
    { inherit overlay; } // inputs.flake-utils.lib.eachDefaultSystem perSystem;
}
