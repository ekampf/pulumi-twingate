// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";

export interface TwingateResourceProtocols {
    allowIcmp?: pulumi.Input<boolean>;
    tcp: pulumi.Input<inputs.TwingateResourceProtocolsTcp>;
    udp: pulumi.Input<inputs.TwingateResourceProtocolsUdp>;
}

export interface TwingateResourceProtocolsTcp {
    policy: pulumi.Input<string>;
    ports?: pulumi.Input<pulumi.Input<string>[]>;
}

export interface TwingateResourceProtocolsUdp {
    policy: pulumi.Input<string>;
    ports?: pulumi.Input<pulumi.Input<string>[]>;
}
