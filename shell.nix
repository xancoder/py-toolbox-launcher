let
  nixpkgs = fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-23.11";
  pkgs = import nixpkgs { config = { allowUnfree = true; }; overlays = []; };
in

pkgs.mkShell {
  name="dev-env-py-toolbox-launcher";
  packages = with pkgs; [
    jetbrains.pycharm-professional
    poetry
    python311
    python311Packages.inquirerpy
    powershell
    inkscape
    imagemagick
  ];
  shellHook = ''
echo "enjoy developing"
which python
which poetry
pycharm-professional
'';
}
