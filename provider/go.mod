module github.com/beyondcloud-co/pulumi-proxmox/provider

go 1.16

replace (
	github.com/hashicorp/go-getter v1.5.0 => github.com/hashicorp/go-getter v1.4.0
	github.com/hashicorp/terraform-plugin-sdk/v2 => github.com/pulumi/terraform-plugin-sdk/v2 v2.0.0-20201218231525-9cca98608a5e
)

require (
	github.com/Masterminds/sprig v2.22.0+incompatible // indirect
	github.com/Sirupsen/logrus v1.0.5 // indirect
	github.com/Telmate/terraform-provider-proxmox v0.0.0-20211018205517-c2ca231dbd11 // indirect
	github.com/go-ldap/ldap v3.0.2+incompatible // indirect
	github.com/google/go-cmp v0.5.6 // indirect
	github.com/hashicorp/go-getter v1.5.3 // indirect
	github.com/hashicorp/hcl/v2 v2.10.1 // indirect
	github.com/hashicorp/terraform-plugin-sdk v1.9.1
	github.com/hashicorp/terraform-plugin-sdk/v2 v2.8.0 // indirect
	github.com/pulumi/pulumi-terraform-bridge/v3 v3.9.0
	github.com/pulumi/pulumi/sdk/v3 v3.14.1-0.20211007222624-789e39219452
	github.com/zclconf/go-cty v1.9.1 // indirect
	gopkg.in/asn1-ber.v1 v1.0.0-20181015200546-f715ec2f112d // indirect
	gopkg.in/src-d/go-git.v4 v4.13.1 // indirect
)
