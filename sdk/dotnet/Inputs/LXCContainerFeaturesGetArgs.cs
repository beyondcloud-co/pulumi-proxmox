// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Proxmox.Inputs
{

    public sealed class LXCContainerFeaturesGetArgs : Pulumi.ResourceArgs
    {
        [Input("fuse")]
        public Input<bool>? Fuse { get; set; }

        [Input("keyctl")]
        public Input<bool>? Keyctl { get; set; }

        [Input("mount")]
        public Input<string>? Mount { get; set; }

        [Input("nesting")]
        public Input<bool>? Nesting { get; set; }

        public LXCContainerFeaturesGetArgs()
        {
        }
    }
}
