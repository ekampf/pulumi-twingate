// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Connectors provide connectivity to Remote Networks. This resource type will create the Connector in the Twingate Admin Console, but in order to successfully deploy it, you must also generate Connector tokens that authenticate the Connector with Twingate. For more information, see Twingate's [documentation](https://docs.twingate.com/docs/understanding-access-nodes).
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as pulumi_twingate from "@twingate-labs/pulumi-twingate";
 *
 * const awsNetwork = new twingate.TwingateRemoteNetwork("awsNetwork", {});
 * const awsConnector = new twingate.TwingateConnector("awsConnector", {remoteNetworkId: awsNetwork.id});
 * ```
 *
 * ## Import
 *
 * ```sh
 *  $ pulumi import twingate:index/twingateConnector:TwingateConnector connector Q29ubmVjdG1b0qe0
 * ```
 */
export class TwingateConnector extends pulumi.CustomResource {
    /**
     * Get an existing TwingateConnector resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TwingateConnectorState, opts?: pulumi.CustomResourceOptions): TwingateConnector {
        return new TwingateConnector(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'twingate:index/twingateConnector:TwingateConnector';

    /**
     * Returns true if the given object is an instance of TwingateConnector.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is TwingateConnector {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === TwingateConnector.__pulumiType;
    }

    /**
     * Name of the Connector, if not provided one will be generated
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The ID of the Remote Network to attach the Connector to
     */
    public readonly remoteNetworkId!: pulumi.Output<string>;

    /**
     * Create a TwingateConnector resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: TwingateConnectorArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: TwingateConnectorArgs | TwingateConnectorState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as TwingateConnectorState | undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["remoteNetworkId"] = state ? state.remoteNetworkId : undefined;
        } else {
            const args = argsOrState as TwingateConnectorArgs | undefined;
            if ((!args || args.remoteNetworkId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'remoteNetworkId'");
            }
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["remoteNetworkId"] = args ? args.remoteNetworkId : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(TwingateConnector.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering TwingateConnector resources.
 */
export interface TwingateConnectorState {
    /**
     * Name of the Connector, if not provided one will be generated
     */
    name?: pulumi.Input<string>;
    /**
     * The ID of the Remote Network to attach the Connector to
     */
    remoteNetworkId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a TwingateConnector resource.
 */
export interface TwingateConnectorArgs {
    /**
     * Name of the Connector, if not provided one will be generated
     */
    name?: pulumi.Input<string>;
    /**
     * The ID of the Remote Network to attach the Connector to
     */
    remoteNetworkId: pulumi.Input<string>;
}
