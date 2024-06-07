# CHANGELOG



## v2.13.7 (2024-06-06)

### Documentation

* docs: refactored scan docs ([`08e0978`](https://gitlab.psi.ch/bec/bec/-/commit/08e0978d2b7a137700fa1c552cbe079a290f32f5))

* docs: added test instructions to fly scan tutorial ([`7cd40ff`](https://gitlab.psi.ch/bec/bec/-/commit/7cd40ffcf597e3b64e87d9206468118b400754d7))

* docs: added tutorial for defining a new fly scan ([`df1fe4d`](https://gitlab.psi.ch/bec/bec/-/commit/df1fe4d64f97244862126d218be7fe9e2ebea925))

### Fix

* fix: adapt to pytest-redis 3.1 ([`0a987c0`](https://gitlab.psi.ch/bec/bec/-/commit/0a987c0815a3173e43dce22e2accef0e87ea284d))


## v2.13.6 (2024-06-05)

### Ci

* ci: fixed pytest redis version for now ([`c6f1204`](https://gitlab.psi.ch/bec/bec/-/commit/c6f12042d3a0d00b1ab9c69a17e829adf76a2c12))

### Fix

* fix: handle redis connection failures more gracefully ([`49425c7`](https://gitlab.psi.ch/bec/bec/-/commit/49425c7eed456f446c837e09c4fa88afedba31ae))

* fix(bec_ipython_client): fixed support for loading hlis from plugins ([`45869aa`](https://gitlab.psi.ch/bec/bec/-/commit/45869aab773d4e288f7c2d4152be140f91f5bb79))


## v2.13.5 (2024-06-05)

### Fix

* fix(bec_lib): fixed msg type serialization ([`05c24e8`](https://gitlab.psi.ch/bec/bec/-/commit/05c24e880bfbf2257c973ec4b451f93918290915))


## v2.13.4 (2024-06-05)

### Fix

* fix(bec_ipython_client): fixed gui startup ([`8f4d89e`](https://gitlab.psi.ch/bec/bec/-/commit/8f4d89e7a49dc7ca9cbbe64e832ddef19b418f16))


## v2.13.3 (2024-06-04)

### Fix

* fix(scan_server): fixed order of reported devices in readout priority ([`64ecbb6`](https://gitlab.psi.ch/bec/bec/-/commit/64ecbb6856de8b108e75f9a4bd2736adb5b4ca74))


## v2.13.2 (2024-06-03)

### Fix

* fix(bec_lib): fixed serialization for message endpoints ([`1be3830`](https://gitlab.psi.ch/bec/bec/-/commit/1be38300abcd0c7cc4a5f5dcf3c72cf19deb27d6))


## v2.13.1 (2024-06-03)

### Fix

* fix: fixed support for mv during scan defs; closes #308 ([`835bf50`](https://gitlab.psi.ch/bec/bec/-/commit/835bf5004ad1c9aaec1792ed20f3ffc613584d31))


## v2.13.0 (2024-06-03)

### Documentation

* docs: improved scan stub docs and glossary ([`e04cf65`](https://gitlab.psi.ch/bec/bec/-/commit/e04cf65f9cbcff4ea8fe3676813e4dce663757a4))

### Feature

* feat(scan_server): added set_with_response and request_is_completed stubs ([`8ac80c1`](https://gitlab.psi.ch/bec/bec/-/commit/8ac80c11ce0e83bb782254b06e2552e8a15c1002))

* feat(scan_server): convert arg inputs to supported scan arg types ([`30b4528`](https://gitlab.psi.ch/bec/bec/-/commit/30b4528de5e448a0c3477d49dff727703de3ed17))

### Fix

* fix(scan_server): worker respects use_scan_progress_report ([`3ad46ef`](https://gitlab.psi.ch/bec/bec/-/commit/3ad46efb148ab9c32e34a6500f1f1af0dbd7144c))

* fix(ipython_client): readback callback must listen to instruction RID ([`c4551d3`](https://gitlab.psi.ch/bec/bec/-/commit/c4551d3b953bc97557e285f350e81b000f7c2cbe))

* fix: minor cleanup ([`8d4a066`](https://gitlab.psi.ch/bec/bec/-/commit/8d4a066832dc45d67b77d13b484d7cd2e565c2f9))

* fix(scan_server): fixed default args ([`0f42a49`](https://gitlab.psi.ch/bec/bec/-/commit/0f42a4926de28252f01d9f9fab53244cc099ca21))

* fix(scan_server): simplify scan args ([`005ff56`](https://gitlab.psi.ch/bec/bec/-/commit/005ff5685609b403b35131cdff0380d8e5b2b742))

* fix(bec_lib): convert devices to strings for scan requests ([`3b176f7`](https://gitlab.psi.ch/bec/bec/-/commit/3b176f7b97087fe87fcfaacd4d575c27be4cbcaf))

### Refactor

* refactor(scan_server): cleanup of scan args ([`3acc13a`](https://gitlab.psi.ch/bec/bec/-/commit/3acc13a8c4fa45765c1b29f446c01df21b056135))

### Test

* test(scan_server): added test for convert_arg_input ([`a302844`](https://gitlab.psi.ch/bec/bec/-/commit/a302844d70659e2d1b074a76c2649a2c15bf0754))

* test: added tests for stubs and contlineflyscan ([`8fed5f6`](https://gitlab.psi.ch/bec/bec/-/commit/8fed5f64a09ea28bb911aaf57a96ba4b50498a56))


## v2.12.6 (2024-05-31)

### Fix

* fix: end the color sequence ([`22be4c4`](https://gitlab.psi.ch/bec/bec/-/commit/22be4c4c6b54133277411e837e9c102aa39685d3))


## v2.12.5 (2024-05-28)

### Fix

* fix: remove deprecated arg speed from deviceconfig ([`67f0bea`](https://gitlab.psi.ch/bec/bec/-/commit/67f0beac75bbeecf69768662e373b96a0839f122))


## v2.12.4 (2024-05-28)

### Ci

* ci: added development pages ([`4a9f4f8`](https://gitlab.psi.ch/bec/bec/-/commit/4a9f4f83fae16f40df679cddc5bf816e3b77deff))

### Documentation

* docs: fixed broken links ([`5dfcbe6`](https://gitlab.psi.ch/bec/bec/-/commit/5dfcbe6d132dd199be9f42980ed254efb2dc0e82))

* docs: added reference to gitlab issues ([`7277ac3`](https://gitlab.psi.ch/bec/bec/-/commit/7277ac3c40f86ff465f7af69a060fb9d5f2d4acc))

* docs: fixed api reference; added reference to scanbase ([`121e592`](https://gitlab.psi.ch/bec/bec/-/commit/121e5922eb3806eff88f49b5378b1f12056be132))

* docs: cleanup ([`7254755`](https://gitlab.psi.ch/bec/bec/-/commit/7254755aacda0f9c50b09237a59cd3584fb48e74))

* docs: added reference to user docs for loading new device configs ([`fd29dfb`](https://gitlab.psi.ch/bec/bec/-/commit/fd29dfb5f7d63d864e08adae1b5128f0f0fed14a))

* docs: added linkify ([`3a363f5`](https://gitlab.psi.ch/bec/bec/-/commit/3a363f5f52b644bc2542913cf4e9acf224ef69f9))

* docs: improvements for the dev docs ([`e5a98d7`](https://gitlab.psi.ch/bec/bec/-/commit/e5a98d718d06004819b32db1fabf77e634bdefd0))

* docs: restructured developer docs ([`7fd66f8`](https://gitlab.psi.ch/bec/bec/-/commit/7fd66f895905cb3e46ee90b98bfac8985837d6ca))

* docs: added docs for developing scans ([`5f44521`](https://gitlab.psi.ch/bec/bec/-/commit/5f4452110519404573484d2c6a95d8a46c325a1f))

* docs: fixed dependency for building sphinx ([`9cbde72`](https://gitlab.psi.ch/bec/bec/-/commit/9cbde72505723b5e4da94eeab4c8313e29c295c5))

* docs: fixed api reference ([`29862dc`](https://gitlab.psi.ch/bec/bec/-/commit/29862dca51873d4c22db6a693014ecf7addb4447))

### Fix

* fix: create readme for tests_dap_services ([`104c847`](https://gitlab.psi.ch/bec/bec/-/commit/104c847b55427c3ac78afb3af9e71154deff7d9e))

### Refactor

* refactor: renamed move_and_wait to move_scan_motors_and_wait ([`eaa8bd8`](https://gitlab.psi.ch/bec/bec/-/commit/eaa8bd8e67aa75a00d6a5b3e2494ed9828e7d6cf))
