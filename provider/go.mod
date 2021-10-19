module github.com/beyondcloud-co/pulumi-proxmox/provider

go 1.16

replace github.com/hashicorp/go-getter v1.5.0 => github.com/hashicorp/go-getter v1.4.0

require (
	github.com/Telmate/terraform-provider-proxmox v0.0.0-20211018205517-c2ca231dbd11 // indirect
	github.com/google/go-cmp v0.5.6 // indirect
	github.com/hashicorp/hcl/v2 v2.10.1 // indirect
	github.com/hashicorp/terraform-plugin-sdk v1.9.1
	github.com/pulumi/pulumi-terraform-bridge/v3 v3.2.1
	github.com/pulumi/pulumi/sdk/v3 v3.4.0
	github.com/zclconf/go-cty v1.9.1 // indirect
)
