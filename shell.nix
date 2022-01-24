{ jdk ? "jdk11" }:

let

  nixpkgs = builtins.fetchTarball {
    name   = "nixos-unstable-2021-12-27";
    url    = "https://github.com/NixOS/nixpkgs/archive/be5272250926e352427b3c62c6066a95c6592375.tar.gz";
    sha256 = "0rda00l8rdf0a4pdsflg0h7dx6hd52291ymcqv1wljzs9k5zsy7i";
  };

  pkgs      = import nixpkgs { inherit jdk; };
  stdenv    = pkgs.stdenv;
  optionals = pkgs.lib.optionals;

  buildPulumi =
    { package
    }:
      pkgs.stdenv.mkDerivation {
        name = "pulumi";
        src = package;
        phases = [ "installPhase" ];
        installPhase = ''
          mkdir -p $out/bin
          tar xvf $src -C $out/bin/
          mv $out/bin/pulumi $out/bin/pulumi-tmp
          mv $out/bin/pulumi-tmp/* $out/bin/
          rm -r $out/bin/pulumi-tmp
          chmod +x $out/bin/pulumi
        '';
      };

  buildPulumictl =
    { package
    }:
      pkgs.stdenv.mkDerivation {
        name = "pulumictl";
        src = package;
        phases = [ "installPhase" ];
        installPhase = ''
          mkdir -p $out/bin
          tar xvf $src -C $out/bin/
          chmod +x $out/bin/pulumictl
        '';
      };


  pulumi-linux = buildPulumi {
    package = pkgs.fetchurl {
      url    = "https://github.com/pulumi/pulumi/releases/download/v3.22.1/pulumi-v3.22.1-linux-x64.tar.gz";
      sha256 = "0yxjlkvyxap4c7ny5x0ch0j4d5360qapb670f6im7vnaqhc00by0";
    };
  };

  pulumi-darwin = buildPulumi {
    package = pkgs.fetchurl {
      url    = "https://github.com/pulumi/pulumi/releases/download/v3.22.1/pulumi-v3.22.1-darwin-x64.tar.gz";
      sha256 = "0b68pfrd83x02rs2saybxycpkirjciilp4a94ps3788y1plinyih";
    };
  };

  pulumictl-linux = buildPulumictl {
    package = pkgs.fetchurl {
      url    = "https://github.com/pulumi/pulumictl/releases/download/v0.0.29/pulumictl-v0.0.29-linux-amd64.tar.gz";
      sha256 = "02i6jx0vrfrhx9ml4rp9ib9lh0hi5l7zssykbz86l9bxdb3xnp85";
    };
  };

  pulumictl-darwin = buildPulumictl {
    package = pkgs.fetchurl {
      url    = "https://github.com/pulumi/pulumictl/releases/download/v0.0.29/pulumictl-v0.0.29-darwin-amd64.tar.gz";
      sha256 = "1pbx8gb1pqm21y3qr29z4byj2lszcgrqhifikss0pvkjnmhsm5a3";
    };
  };


  commonPkgs = with pkgs; [
      curl            # 7.74.0
      git             # 2.30.1
      kubectl         # 1.20.4
      nodejs-16_x     # 16.3.0
      yarn            # 1.22.10
      python3         # 3.8.8
      pwgen           # 2.08
      kubernetes-helm # 3.5.3
      kustomize       # 4.1.3
      unzip
      python38Packages.pip
      python38Packages.virtualenv
      go 
      python38Packages.setuptools
      dotnet-sdk_5
    ];

  darwinPkgs = with pkgs; [
    pulumi-darwin
    pulumictl-darwin
  ];

  linuxPkgs = with pkgs; [
    pulumi-linux
    pulumictl-linux
  ];

  packages = commonPkgs ++ optionals stdenv.isDarwin darwinPkgs ++ optionals stdenv.isLinux linuxPkgs;
in

  pkgs.mkShell {
    buildInputs = packages;

    shellHook = ''
    '';
  }
