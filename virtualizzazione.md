# Virtualizzazione


https://www.makeuseof.com/create-windows-virtual-machine-in-linux-with-kvm/

## installazione/setup kvm

```
grep -Ec '(vmx|svm)' /proc/cpuinfo # controllare sia diverso da 0
        
sudo apt install qemu-kvm libvirt-daemon bridge-utils virt-manager

        
sudo systemctl enable libvirtd
sudo systemctl start libvirtd
usermod -aG libvirt l
usermod -aG kvm l

```

## avviare virt-manager

```
virt-manager
```
