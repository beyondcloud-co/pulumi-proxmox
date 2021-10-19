// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

declare var exports: any;
const __config = new pulumi.Config("proxmox");

/**
 * API TokenID e.g. root@pam!mytesttoken
 */
export declare const pmApiTokenId: string | undefined;
Object.defineProperty(exports, "pmApiTokenId", {
    get() {
        return __config.get("pmApiTokenId");
    },
    enumerable: true,
});

/**
 * The secret uuid corresponding to a TokenID
 */
export declare const pmApiTokenSecret: string | undefined;
Object.defineProperty(exports, "pmApiTokenSecret", {
    get() {
        return __config.get("pmApiTokenSecret");
    },
    enumerable: true,
});

/**
 * https://host.fqdn:8006/api2/json
 */
export declare const pmApiUrl: string | undefined;
Object.defineProperty(exports, "pmApiUrl", {
    get() {
        return __config.get("pmApiUrl");
    },
    enumerable: true,
});

/**
 * By default this provider will exit if an unknown attribute is found. This is to prevent the accidential destruction of
 * VMs or Data when something in the proxmox API has changed/updated and is not confirmed to work with this provider. Set
 * this to true at your own risk. It may allow you to proceed in cases when the provider refuses to work, but be aware of
 * the danger in doing so.
 */
export declare const pmDangerouslyIgnoreUnknownAttributes: boolean | undefined;
Object.defineProperty(exports, "pmDangerouslyIgnoreUnknownAttributes", {
    get() {
        return __config.getObject<boolean>("pmDangerouslyIgnoreUnknownAttributes");
    },
    enumerable: true,
});

/**
 * Enable provider logging to get proxmox API logs
 */
export declare const pmLogEnable: boolean | undefined;
Object.defineProperty(exports, "pmLogEnable", {
    get() {
        return __config.getObject<boolean>("pmLogEnable");
    },
    enumerable: true,
});

/**
 * Write logs to this specific file
 */
export declare const pmLogFile: string | undefined;
Object.defineProperty(exports, "pmLogFile", {
    get() {
        return __config.get("pmLogFile");
    },
    enumerable: true,
});

/**
 * Configure the logging level to display; trace, debug, info, warn, etc
 */
export declare const pmLogLevels: {[key: string]: any} | undefined;
Object.defineProperty(exports, "pmLogLevels", {
    get() {
        return __config.getObject<{[key: string]: any}>("pmLogLevels");
    },
    enumerable: true,
});

/**
 * OTP 2FA code (if required)
 */
export declare const pmOtp: string | undefined;
Object.defineProperty(exports, "pmOtp", {
    get() {
        return __config.get("pmOtp");
    },
    enumerable: true,
});

export declare const pmParallel: number | undefined;
Object.defineProperty(exports, "pmParallel", {
    get() {
        return __config.getObject<number>("pmParallel");
    },
    enumerable: true,
});

/**
 * Password to authenticate into proxmox
 */
export declare const pmPassword: string | undefined;
Object.defineProperty(exports, "pmPassword", {
    get() {
        return __config.get("pmPassword");
    },
    enumerable: true,
});

export declare const pmTimeout: number | undefined;
Object.defineProperty(exports, "pmTimeout", {
    get() {
        return __config.getObject<number>("pmTimeout");
    },
    enumerable: true,
});

/**
 * By default, every TLS connection is verified to be secure. This option allows terraform to proceed and operate on
 * servers considered insecure. For example if you're connecting to a remote host and you do not have the CA cert that
 * issued the proxmox api url's certificate.
 */
export declare const pmTlsInsecure: boolean | undefined;
Object.defineProperty(exports, "pmTlsInsecure", {
    get() {
        return __config.getObject<boolean>("pmTlsInsecure");
    },
    enumerable: true,
});

/**
 * Username e.g. myuser or myuser@pam
 */
export declare const pmUser: string | undefined;
Object.defineProperty(exports, "pmUser", {
    get() {
        return __config.get("pmUser");
    },
    enumerable: true,
});

