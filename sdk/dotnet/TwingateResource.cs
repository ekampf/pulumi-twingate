// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace TwingateLabs.Twingate
{
    /// <summary>
    /// Resources in Twingate represent servers on the private network that clients can connect to. Resources can be defined by IP, CIDR range, FQDN, or DNS zone. For more information, see the Twingate [documentation](https://docs.twingate.com/docs/resources-and-access-nodes).
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Twingate = TwingateLabs.Twingate;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var awsNetwork = new Twingate.TwingateRemoteNetwork("awsNetwork", new Twingate.TwingateRemoteNetworkArgs
    ///         {
    ///         });
    ///         var resource = new Twingate.TwingateResource("resource", new Twingate.TwingateResourceArgs
    ///         {
    ///             Address = "internal.int",
    ///             RemoteNetworkId = awsNetwork.Id,
    ///             GroupIds = 
    ///             {
    ///                 "group1",
    ///             },
    ///             Protocols = new Twingate.Inputs.TwingateResourceProtocolsArgs
    ///             {
    ///                 AllowIcmp = true,
    ///                 Tcp = new Twingate.Inputs.TwingateResourceProtocolsTcpArgs
    ///                 {
    ///                     Policy = "RESTRICTED",
    ///                     Ports = 
    ///                     {
    ///                         "80",
    ///                         "82-83",
    ///                     },
    ///                 },
    ///                 Udp = new Twingate.Inputs.TwingateResourceProtocolsUdpArgs
    ///                 {
    ///                     Policy = "ALLOW_ALL",
    ///                 },
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    [TwingateResourceType("twingate:index/twingateResource:TwingateResource")]
    public partial class TwingateResource : Pulumi.CustomResource
    {
        /// <summary>
        /// The Resource's IP/CIDR or FQDN/DNS zone
        /// </summary>
        [Output("address")]
        public Output<string> Address { get; private set; } = null!;

        /// <summary>
        /// List of Group IDs that have permission to access the Resource, cannot be generated by Terraform and must be retrieved
        /// from the Twingate Admin Console or API
        /// </summary>
        [Output("groupIds")]
        public Output<ImmutableArray<string>> GroupIds { get; private set; } = null!;

        /// <summary>
        /// The name of the Resource
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Restrict access to certain protocols and ports. By default or when this argument is not defined, there is no
        /// restriction, and all protocols and ports are allowed.
        /// </summary>
        [Output("protocols")]
        public Output<Outputs.TwingateResourceProtocols?> Protocols { get; private set; } = null!;

        /// <summary>
        /// Remote Network ID where the Resource lives
        /// </summary>
        [Output("remoteNetworkId")]
        public Output<string> RemoteNetworkId { get; private set; } = null!;


        /// <summary>
        /// Create a TwingateResource resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public TwingateResource(string name, TwingateResourceArgs args, CustomResourceOptions? options = null)
            : base("twingate:index/twingateResource:TwingateResource", name, args ?? new TwingateResourceArgs(), MakeResourceOptions(options, ""))
        {
        }

        private TwingateResource(string name, Input<string> id, TwingateResourceState? state = null, CustomResourceOptions? options = null)
            : base("twingate:index/twingateResource:TwingateResource", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "https://github.com/Twingate-Labs/pulumi-twingate/releases/download/v${VERSION}",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing TwingateResource resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static TwingateResource Get(string name, Input<string> id, TwingateResourceState? state = null, CustomResourceOptions? options = null)
        {
            return new TwingateResource(name, id, state, options);
        }
    }

    public sealed class TwingateResourceArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Resource's IP/CIDR or FQDN/DNS zone
        /// </summary>
        [Input("address", required: true)]
        public Input<string> Address { get; set; } = null!;

        [Input("groupIds")]
        private InputList<string>? _groupIds;

        /// <summary>
        /// List of Group IDs that have permission to access the Resource, cannot be generated by Terraform and must be retrieved
        /// from the Twingate Admin Console or API
        /// </summary>
        public InputList<string> GroupIds
        {
            get => _groupIds ?? (_groupIds = new InputList<string>());
            set => _groupIds = value;
        }

        /// <summary>
        /// The name of the Resource
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Restrict access to certain protocols and ports. By default or when this argument is not defined, there is no
        /// restriction, and all protocols and ports are allowed.
        /// </summary>
        [Input("protocols")]
        public Input<Inputs.TwingateResourceProtocolsArgs>? Protocols { get; set; }

        /// <summary>
        /// Remote Network ID where the Resource lives
        /// </summary>
        [Input("remoteNetworkId", required: true)]
        public Input<string> RemoteNetworkId { get; set; } = null!;

        public TwingateResourceArgs()
        {
        }
    }

    public sealed class TwingateResourceState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Resource's IP/CIDR or FQDN/DNS zone
        /// </summary>
        [Input("address")]
        public Input<string>? Address { get; set; }

        [Input("groupIds")]
        private InputList<string>? _groupIds;

        /// <summary>
        /// List of Group IDs that have permission to access the Resource, cannot be generated by Terraform and must be retrieved
        /// from the Twingate Admin Console or API
        /// </summary>
        public InputList<string> GroupIds
        {
            get => _groupIds ?? (_groupIds = new InputList<string>());
            set => _groupIds = value;
        }

        /// <summary>
        /// The name of the Resource
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Restrict access to certain protocols and ports. By default or when this argument is not defined, there is no
        /// restriction, and all protocols and ports are allowed.
        /// </summary>
        [Input("protocols")]
        public Input<Inputs.TwingateResourceProtocolsGetArgs>? Protocols { get; set; }

        /// <summary>
        /// Remote Network ID where the Resource lives
        /// </summary>
        [Input("remoteNetworkId")]
        public Input<string>? RemoteNetworkId { get; set; }

        public TwingateResourceState()
        {
        }
    }
}
