// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package config

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

// The access key for API operations. You can retrieve this from the Twingate Admin Console
// ([documentation](https://docs.twingate.com/docs/api-overview)). Alternatively, this can be specified using the
// TWINGATE_API_TOKEN environment variable.
func GetApiToken(ctx *pulumi.Context) string {
	return config.Get(ctx, "twingate:apiToken")
}

// Specifies a retry limit for the http requests made. This setting is 5. Alternatively, this can be specified using the
// TWINGATE_HTTP_MAX_RETRY environment variable
func GetHttpMaxRetry(ctx *pulumi.Context) int {
	v, err := config.TryInt(ctx, "twingate:httpMaxRetry")
	if err == nil {
		return v
	}
	return 5
}

// Specifies a time limit in seconds for the http requests made. The default value is 10 seconds. Alternatively, this can
// be specified using the TWINGATE_HTTP_TIMEOUT environment variable
func GetHttpTimeout(ctx *pulumi.Context) int {
	v, err := config.TryInt(ctx, "twingate:httpTimeout")
	if err == nil {
		return v
	}
	return 10
}

// Your Twingate network ID for API operations. You can find it in the Admin Console URL, for example:
// `autoco.twingate.com`, where `autoco` is your network ID Alternatively, this can be specified using the TWINGATE_NETWORK
// environment variable.
func GetNetwork(ctx *pulumi.Context) string {
	return config.Get(ctx, "twingate:network")
}

// The default is 'twingate.com' This is optional and shouldn't be changed under normal circumstances.
func GetUrl(ctx *pulumi.Context) string {
	return config.Get(ctx, "twingate:url")
}
