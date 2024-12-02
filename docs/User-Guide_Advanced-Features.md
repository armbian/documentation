# Advanced Features

## How to switch kernels?

```bash
armbian-config --cmd SY015
```
## How to build a wireless driver?

Install kernel headers:

	armbian-config --cmd SY004

Download driver sources:

        git clone https://github.com/morrownr/8821au-20210708.git
        cd 8821au-20210708

Build and install:

        make
        make install

??? "Build log"

    ```
    make ARCH=arm64 CROSS_COMPILE= -C /lib/modules/6.6.62-current-sunxi64/build M=/root/8821au-20210708  modules
    make[1]: Entering directory '/usr/src/linux-headers-6.6.62-current-sunxi64'
      CC [M]  /root/8821au-20210708/core/rtw_cmd.o
      CC [M]  /root/8821au-20210708/core/rtw_security.o
      CC [M]  /root/8821au-20210708/core/rtw_debug.o
      CC [M]  /root/8821au-20210708/core/rtw_io.o
      CC [M]  /root/8821au-20210708/core/rtw_ioctl_query.o
      CC [M]  /root/8821au-20210708/core/rtw_ioctl_set.o
      CC [M]  /root/8821au-20210708/core/rtw_ieee80211.o
      CC [M]  /root/8821au-20210708/core/rtw_mlme.o
      CC [M]  /root/8821au-20210708/core/rtw_mlme_ext.o
      CC [M]  /root/8821au-20210708/core/rtw_mi.o
      CC [M]  /root/8821au-20210708/core/rtw_wlan_util.o
      CC [M]  /root/8821au-20210708/core/rtw_vht.o
      CC [M]  /root/8821au-20210708/core/rtw_pwrctrl.o
      CC [M]  /root/8821au-20210708/core/rtw_rf.o
      CC [M]  /root/8821au-20210708/core/rtw_chplan.o
      CC [M]  /root/8821au-20210708/core/monitor/rtw_radiotap.o
      CC [M]  /root/8821au-20210708/core/rtw_recv.o
      CC [M]  /root/8821au-20210708/core/rtw_sta_mgt.o
      CC [M]  /root/8821au-20210708/core/rtw_ap.o
      CC [M]  /root/8821au-20210708/core/wds/rtw_wds.o
      CC [M]  /root/8821au-20210708/core/mesh/rtw_mesh.o
      CC [M]  /root/8821au-20210708/core/mesh/rtw_mesh_pathtbl.o
      CC [M]  /root/8821au-20210708/core/mesh/rtw_mesh_hwmp.o
      CC [M]  /root/8821au-20210708/core/rtw_xmit.o
      CC [M]  /root/8821au-20210708/core/rtw_p2p.o
      CC [M]  /root/8821au-20210708/core/rtw_rson.o
      CC [M]  /root/8821au-20210708/core/rtw_tdls.o
      CC [M]  /root/8821au-20210708/core/rtw_br_ext.o
      CC [M]  /root/8821au-20210708/core/rtw_iol.o
      CC [M]  /root/8821au-20210708/core/rtw_sreset.o
      CC [M]  /root/8821au-20210708/core/rtw_btcoex_wifionly.o
      CC [M]  /root/8821au-20210708/core/rtw_btcoex.o
      CC [M]  /root/8821au-20210708/core/rtw_beamforming.o
      CC [M]  /root/8821au-20210708/core/rtw_odm.o
      CC [M]  /root/8821au-20210708/core/rtw_rm.o
      CC [M]  /root/8821au-20210708/core/rtw_rm_fsm.o
      CC [M]  /root/8821au-20210708/core/rtw_ft.o
      CC [M]  /root/8821au-20210708/core/rtw_wnm.o
      CC [M]  /root/8821au-20210708/core/rtw_mbo.o
      CC [M]  /root/8821au-20210708/core/rtw_rm_util.o
      CC [M]  /root/8821au-20210708/core/efuse/rtw_efuse.o
      CC [M]  /root/8821au-20210708/core/rtw_roch.o
      CC [M]  /root/8821au-20210708/core/crypto/aes-internal.o
      CC [M]  /root/8821au-20210708/core/crypto/aes-internal-enc.o
      CC [M]  /root/8821au-20210708/core/crypto/aes-gcm.o
      CC [M]  /root/8821au-20210708/core/crypto/aes-ccm.o
      CC [M]  /root/8821au-20210708/core/crypto/aes-omac1.o
      CC [M]  /root/8821au-20210708/core/crypto/ccmp.o
      CC [M]  /root/8821au-20210708/core/crypto/gcmp.o
      CC [M]  /root/8821au-20210708/core/crypto/aes-siv.o
      CC [M]  /root/8821au-20210708/core/crypto/aes-ctr.o
      CC [M]  /root/8821au-20210708/core/crypto/sha256-internal.o
      CC [M]  /root/8821au-20210708/core/crypto/sha256.o
      CC [M]  /root/8821au-20210708/core/crypto/sha256-prf.o
      CC [M]  /root/8821au-20210708/core/crypto/rtw_crypto_wrap.o
      CC [M]  /root/8821au-20210708/core/rtw_swcrypto.o
      CC [M]  /root/8821au-20210708/os_dep/osdep_service.o
      CC [M]  /root/8821au-20210708/os_dep/linux/os_intfs.o
      CC [M]  /root/8821au-20210708/os_dep/linux/usb_intf.o
      CC [M]  /root/8821au-20210708/os_dep/linux/usb_ops_linux.o
      CC [M]  /root/8821au-20210708/os_dep/linux/ioctl_linux.o
      CC [M]  /root/8821au-20210708/os_dep/linux/xmit_linux.o
      CC [M]  /root/8821au-20210708/os_dep/linux/mlme_linux.o
      CC [M]  /root/8821au-20210708/os_dep/linux/recv_linux.o
      CC [M]  /root/8821au-20210708/os_dep/linux/ioctl_cfg80211.o
      CC [M]  /root/8821au-20210708/os_dep/linux/rtw_cfgvendor.o
      CC [M]  /root/8821au-20210708/os_dep/linux/wifi_regd.o
      CC [M]  /root/8821au-20210708/os_dep/linux/rtw_android.o
      CC [M]  /root/8821au-20210708/os_dep/linux/rtw_proc.o
      CC [M]  /root/8821au-20210708/os_dep/linux/nlrtw.o
      CC [M]  /root/8821au-20210708/os_dep/linux/rtw_rhashtable.o
      CC [M]  /root/8821au-20210708/hal/hal_intf.o
      CC [M]  /root/8821au-20210708/hal/hal_com.o
      CC [M]  /root/8821au-20210708/hal/hal_com_phycfg.o
      CC [M]  /root/8821au-20210708/hal/hal_phy.o
      CC [M]  /root/8821au-20210708/hal/hal_dm.o
      CC [M]  /root/8821au-20210708/hal/hal_dm_acs.o
      CC [M]  /root/8821au-20210708/hal/hal_btcoex_wifionly.o
      CC [M]  /root/8821au-20210708/hal/hal_btcoex.o
      CC [M]  /root/8821au-20210708/hal/hal_mp.o
      CC [M]  /root/8821au-20210708/hal/hal_mcc.o
      CC [M]  /root/8821au-20210708/hal/hal_hci/hal_usb.o
      CC [M]  /root/8821au-20210708/hal/led/hal_led.o
      CC [M]  /root/8821au-20210708/hal/led/hal_usb_led.o
      CC [M]  /root/8821au-20210708/hal/HalPwrSeqCmd.o
      CC [M]  /root/8821au-20210708/hal/rtl8812a/Hal8812PwrSeq.o
      CC [M]  /root/8821au-20210708/hal/rtl8812a/Hal8821APwrSeq.o
      CC [M]  /root/8821au-20210708/hal/rtl8812a/rtl8812a_xmit.o
      CC [M]  /root/8821au-20210708/hal/rtl8812a/rtl8812a_sreset.o
      CC [M]  /root/8821au-20210708/hal/rtl8812a/rtl8812a_hal_init.o
      CC [M]  /root/8821au-20210708/hal/rtl8812a/rtl8812a_phycfg.o
      CC [M]  /root/8821au-20210708/hal/rtl8812a/rtl8812a_rf6052.o
      CC [M]  /root/8821au-20210708/hal/rtl8812a/rtl8812a_dm.o
      CC [M]  /root/8821au-20210708/hal/rtl8812a/rtl8812a_rxdesc.o
      CC [M]  /root/8821au-20210708/hal/rtl8812a/rtl8812a_cmd.o
      CC [M]  /root/8821au-20210708/hal/rtl8812a/usb/usb_halinit.o
      CC [M]  /root/8821au-20210708/hal/rtl8812a/usb/rtl8812au_led.o
      CC [M]  /root/8821au-20210708/hal/rtl8812a/usb/rtl8812au_xmit.o
      CC [M]  /root/8821au-20210708/hal/rtl8812a/usb/rtl8812au_recv.o
      CC [M]  /root/8821au-20210708/hal/rtl8812a/usb/usb_ops_linux.o
      CC [M]  /root/8821au-20210708/hal/efuse/rtl8812a/HalEfuseMask8821A_USB.o
      CC [M]  /root/8821au-20210708/hal/rtl8812a/hal8821a_fw.o
      CC [M]  /root/8821au-20210708/hal/phydm/phydm_debug.o
      CC [M]  /root/8821au-20210708/hal/phydm/phydm_antdiv.o
      CC [M]  /root/8821au-20210708/hal/phydm/phydm_soml.o
      CC [M]  /root/8821au-20210708/hal/phydm/phydm_smt_ant.o
      CC [M]  /root/8821au-20210708/hal/phydm/phydm_antdect.o
      CC [M]  /root/8821au-20210708/hal/phydm/phydm_interface.o
      CC [M]  /root/8821au-20210708/hal/phydm/phydm_phystatus.o
      CC [M]  /root/8821au-20210708/hal/phydm/phydm_hwconfig.o
      CC [M]  /root/8821au-20210708/hal/phydm/phydm.o
      CC [M]  /root/8821au-20210708/hal/phydm/phydm_dig.o
      CC [M]  /root/8821au-20210708/hal/phydm/phydm_pathdiv.o
      CC [M]  /root/8821au-20210708/hal/phydm/phydm_rainfo.o
      CC [M]  /root/8821au-20210708/hal/phydm/phydm_dynamictxpower.o
      CC [M]  /root/8821au-20210708/hal/phydm/phydm_adaptivity.o
      CC [M]  /root/8821au-20210708/hal/phydm/phydm_cfotracking.o
      CC [M]  /root/8821au-20210708/hal/phydm/phydm_noisemonitor.o
      CC [M]  /root/8821au-20210708/hal/phydm/phydm_beamforming.o
      CC [M]  /root/8821au-20210708/hal/phydm/phydm_direct_bf.o
      CC [M]  /root/8821au-20210708/hal/phydm/phydm_dfs.o
      CC [M]  /root/8821au-20210708/hal/phydm/txbf/halcomtxbf.o
      CC [M]  /root/8821au-20210708/hal/phydm/txbf/haltxbfinterface.o
      CC [M]  /root/8821au-20210708/hal/phydm/txbf/phydm_hal_txbf_api.o
      CC [M]  /root/8821au-20210708/hal/phydm/phydm_adc_sampling.o
      CC [M]  /root/8821au-20210708/hal/phydm/phydm_ccx.o
      CC [M]  /root/8821au-20210708/hal/phydm/phydm_psd.o
      CC [M]  /root/8821au-20210708/hal/phydm/phydm_primary_cca.o
      CC [M]  /root/8821au-20210708/hal/phydm/phydm_cck_pd.o
      CC [M]  /root/8821au-20210708/hal/phydm/phydm_rssi_monitor.o
      CC [M]  /root/8821au-20210708/hal/phydm/phydm_auto_dbg.o
      CC [M]  /root/8821au-20210708/hal/phydm/phydm_math_lib.o
      CC [M]  /root/8821au-20210708/hal/phydm/phydm_api.o
      CC [M]  /root/8821au-20210708/hal/phydm/phydm_pow_train.o
      CC [M]  /root/8821au-20210708/hal/phydm/phydm_lna_sat.o
      CC [M]  /root/8821au-20210708/hal/phydm/phydm_pmac_tx_setting.o
      CC [M]  /root/8821au-20210708/hal/phydm/phydm_mp.o
      CC [M]  /root/8821au-20210708/hal/phydm/phydm_cck_rx_pathdiv.o
      CC [M]  /root/8821au-20210708/hal/phydm/halrf/halrf.o
      CC [M]  /root/8821au-20210708/hal/phydm/halrf/halrf_debug.o
      CC [M]  /root/8821au-20210708/hal/phydm/halrf/halphyrf_ce.o
      CC [M]  /root/8821au-20210708/hal/phydm/halrf/halrf_powertracking_ce.o
      CC [M]  /root/8821au-20210708/hal/phydm/halrf/halrf_powertracking.o
      CC [M]  /root/8821au-20210708/hal/phydm/halrf/halrf_kfree.o
      CC [M]  /root/8821au-20210708/hal/phydm/halrf/halrf_psd.o
      CC [M]  /root/8821au-20210708/hal/phydm/rtl8821a/halhwimg8821a_mac.o
      CC [M]  /root/8821au-20210708/hal/phydm/rtl8821a/halhwimg8821a_bb.o
      CC [M]  /root/8821au-20210708/hal/phydm/rtl8821a/halhwimg8821a_rf.o
      CC [M]  /root/8821au-20210708/hal/phydm/halrf/rtl8812a/halrf_8812a_ce.o
      CC [M]  /root/8821au-20210708/hal/phydm/halrf/rtl8821a/halrf_8821a_ce.o
      CC [M]  /root/8821au-20210708/hal/phydm/rtl8821a/phydm_regconfig8821a.o
      CC [M]  /root/8821au-20210708/hal/phydm/rtl8821a/phydm_rtl8821a.o
      CC [M]  /root/8821au-20210708/hal/phydm/halrf/rtl8821a/halrf_iqk_8821a_ce.o
      CC [M]  /root/8821au-20210708/hal/phydm/txbf/haltxbfjaguar.o
      CC [M]  /root/8821au-20210708/hal/btc/halbtc8821a1ant.o
      CC [M]  /root/8821au-20210708/hal/btc/halbtc8821a2ant.o
      CC [M]  /root/8821au-20210708/platform/platform_ops.o
      LD [M]  /root/8821au-20210708/8821au.o
      MODPOST /root/8821au-20210708/Module.symvers
      CC [M]  /root/8821au-20210708/8821au.mod.o
      LD [M]  /root/8821au-20210708/8821au.ko
    make[1]: Leaving directory '/usr/src/linux-headers-6.6.62-current-sunxi64'
    ```

Load driver for test

	insmod 8821au.ko

Check `dmesg` and the last entry will be:

	usbcore: registered new interface driver rtl8821au

Plug the USB wireless adaptor and proceed with [network configuration](/User-Guide_Networking/)

## How to install Docker?

Minimal:

```bash
armbian-config --CON01
```

Full featured:

```bash
armbian-config --CON02
```

Test if Docker works correctly:

```bash
docker run hello-world
```

If you get that kind of output, then Docker install went fine:

```bash
Hello from Docker!
This message shows that your installation appears to be working correctly.
```