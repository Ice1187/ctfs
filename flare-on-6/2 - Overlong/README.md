
## 2 - Overlong 
### Description 
> The secret of this next challenge is cleverly hidden. However, with the right approach, finding the solution will not take an <b>overlong</b> amount of time.

### Environment

- radare2

### Solution

1. r2 打開，直接看到 flag (???

2. 在`0x402008`的位址放了encode的資料，跑起來就會自動decode。（應該是某種標準的編碼方式，可以被radare2自動decode）

FLAG: `I_a_M_t_h_e_e_n_C_o_D_i_n_g_flare_on.com`


### Reference

