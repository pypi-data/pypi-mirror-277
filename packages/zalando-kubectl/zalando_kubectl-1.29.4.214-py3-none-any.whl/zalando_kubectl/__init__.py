# This is replaced during release process.
__version_suffix__ = '214'

APP_NAME = "zalando-kubectl"

KUBECTL_VERSION = "v1.29.4"
KUBECTL_SHA512 = {
    "linux": "c13235bd929eaaf4d0eaaa9ba883e95ce27a402ca7256c634e20a027fbf72db8834de8ea2ca7238e1fe92859e0edc7384a1cec7fbe2b7a5adf07b2e5cf99b04f",
    "darwin": "01506990cf76344fb12207e3e88a7c38a926ad8ccffc00b0ddcfeff9a5312b01438ef8c813e877e4b856cf1cc3f52dada7cd687a487797168a3436b66c64fc9b",
}
STERN_VERSION = "1.26.0"
STERN_SHA256 = {
    "linux": "de79474d9197582e38da0dccc8cd14af23d6b52b72bee06b62943c19ab95125e",
    "darwin": "f89631ea73659e1db4e9d8ef94c58cd2c4e92d595e5d2b7be9184f86e755ee95",
}
KUBELOGIN_VERSION = "v1.28.1"
KUBELOGIN_SHA256 = {
    "linux": "d17dafa1aaa8ede96a81a155cebd7dfd6a0ef6d38c7f76f3d67a57effd94775a",
    "darwin": "7150c0ce6df9e22f958ea07ac64cafdaef8a5f66ad0abe22fbe7f5fb6dbb677e",
}
ZALANDO_AWS_CLI_VERSION = "0.5.4"
ZALANDO_AWS_CLI_SHA256 = {
    "linux": "a19e869cc026ed22c3dc043cd3526e436a89635dc247c81dc76ce4f2150ed22a",
    "darwin": "64a1c084fe913748e4260f783158ffabb4b6b60550996671e254fa727b93f5e5",
}

APP_VERSION = KUBECTL_VERSION + "." + __version_suffix__
