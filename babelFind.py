import pybel
import os

numbers = [3, 4, 1, 6, 20, 98]
with open ("latestAnswers.txt", "r+") as possibleNames:
    for hexName in possibleNames.readlines():
        hexName=((hexName.strip(",")).strip("\n")).strip()
        for wall in numbers:
            if (wall < 1) or (wall > 4):
                continue
            for shelf in numbers:
                if (shelf < 1) or (shelf > 4):
                    continue
                for volume in numbers:
                    if (volume < 1) or (volume > 32):
                        continue
                    wholeBook = (pybel.getbook(hexName.lower(), str(wall), str(shelf), str(volume))).split("\n\n")
                    for page in numbers:
                        os.system("cls")
                        try:
                            #if "archivist" in wholeBook[page-1]:
                            print(f"HexName: {hexName.lower()}\tWall: {wall}\t\tShelf: {shelf}\tVolume: {volume}\tPage: {page}")
                            print(f"{wholeBook[page-1]}\n")
                            input("Press Enter to continue...\n")
                        except:
                            print(f"ERROR:\tHexName: {hexName.lower()}\tWall: {wall}\t\tShelf: {shelf}\tVolume: {volume}\tPage: {page}")
                            continue

                        




#hexName = "20ssaxrfxkwqj84zqzfp5b3mvbkzht41hnwu6sswp79gzklwaex1ld25z91r425ewcqvmcca1mqpzx899f372gsb00mtovxihg37y059qgff7foplekbbapf2sg4v25gbc0rye10iimgfq4ftu3rxhfwbya124dsxk5d214qdcnxdqyhgffhpq0vzjrrxqjdgotregb3u93ruaeajh587f8a41zocpka5nnzf6n72szdaytiw111432jx9xfm03e2rggl7c6sbk5fn041dv7t7e1jg2y7cka4e41s286lk18999ff42xd1fkjxg7zd36ldl7t5a49lrbb8jzr3jbh7oqr6s1ljp8oo226ylbr3lf0istlj6gahoed18aff4lafjg9ju1agk6ibcj6fktx3lfqlbfysf27c6fx8bv7ka22nzjqpb8xednmiahzpt5fhcgyyoifzwkbwlobt7ahjvm35xt5j1tglwnpqz04q6nfagenfce7nqs5kedsy170krs3v6mv4860x37ww70zmgypg0mijzzcwz3egript41181jutlthbj25qb8095yh4h39cc3452hb8ggxsi4jcewjbnr2q7ku4j1zoa1xzamfnzpm7z2jwmsh6mubzpm7rqdg6vdcr9dlvsw2fe7xjb8dbgntgjiaj74ra8nx9wsr4yioxncls71vy9akes02ru0rrcap49owgyaqbah4tq0w48oks04k24r19330bx8071dpks1ude15s6f6ptwdp6umgcwbe1btwddvw52lt8r4d904xidnz67xl684ktyn7d96yca3iuevhqhmolqw780o0dfeupg2u024i13kfvtxrvg6f3s9ii3tfg94nv0ipcsjfm9mwwbnyn532bzwatbla8h7ec4g972r3s0vzspo8d322bl8hi6wv84ropbseqx3mkhpkicyumx7f4j8lxsfmd2037z2su8aa8wvf0i437it3ek6n5ys5vbjpf4ycan6f8y7zpg59sfwnsi3692jouvbg1tazvq595cpqjoxdq9rcafzlag2yshytifhxrw8y7wjpz3j53dxsqv8wknuw8qdk3z4pcr1yveoqjehkfr8rl87avhgazn4ppwa6xye0rlswhvwo5oc9kkbb78qd3is3wrw1kgt4ao2mq7c2q5p47vgpn89mjparjpfsscwungln3eifzphrp5izzxrrme16n5p2l0zg6nr8rlzwrdxm1qkon7xijx00zbnq7eua9bx2uc00nf0i5yljdg4a0h6zdgwnvjptqdgc6xnlrt9cnint8lyea88freo5kdp1sjikw3jbmjjji6rw24tl23z54prj2kb570f3qw7hhzcggz6ghiw0p4e3abfdqdmcivrhzi31ftq60ksu1t46r15zpq7lgmj98vf6c8nez8r666gvce171t5jyfga0fh13buwtpkbq23a0wanlz2q0fwyho4icrlgsdd5a24w1prmey80fbjd0njftrtal85yrwi19ksgelq2fclzz8x0n927ddv37lpr4cxmg2rrc6u7a7niel9ummwzgyxw9lmvwr59wqediksci74oavovswv7txayiud6lhpgj7196vuz7dd3eopdm4hifk2hqb144ik5mc72vkx1sxm3wkd9q5xe58tt8mguztrgddvud29psmbvua1dp0ltg68c0qqsr9ddo48mdc6l3grze4l35kfdiz58ns7n78j9ksftp3n0ahqerl4h380p29cihwltix33lysx86vxrc43bgd2bke7wvn6p7ijjpwjyt68h6kdjdgrc75a3d43pfyw0ezdx32lt1375hme2pgjw0sfzkqqdchirkvbdw3v9dm6m6w3tar4x7xzv3kku8uldl0h976v2hxdq7mg3gxxqt8ednvgcx5t6h6dchfdzru8mgmew33cc1twxjfc76cm8xl8w15tmbitox75f9upzsz8zlzrjaspgas24xuqnm9pla1yhyekdpsnsnbgibmz2c9o8xa2ic03gf7ixhfz7g6dukextn4r6uv9kdq02k3b0v2zhdzxgnntb05m19k9a1otieg5eu2zr6cy6t7ku752u5bymp5oalik5dddl94epg1et0k5ij8yl0wj5w0bdve9z397pwy5z131702btng868a2efy8389t9ffp3ap67xyqmniuai363vpb83ctetgfdvledg968tqjt91j19ooa0t4gka29xhlp8olvfzoy0zk4h4qaelkykdsxjbxzunjhrjpznourfrbudom8i5nzrbcyetso5nyi7rgs1b2n15qyixukd5cx1o4fvj8mkd22ot0g8aga2elx08lu0dbxbvniq7b54gfral0ebab8tfyo21d7xwo1dlqrt3qbbwj7jt9rj2s2l6l6lb61zwm2dx2bb61mg2k9ie56y0jg6hrpwh4qb6zyrr5obc6099dz6uydqav94966yefvj55h2e6zr416vzn89k4erz1b7kulgxiehr7y74uwzpk8c6cth3g4vt1akzknaz6fb602oo9pc0r77opnm75wea7hbmfdzfewmvoeyl74vwzgs9r1gs1jdctmhkzeq4isj2uzzcfrm8paglpx7eazijo60f9n9g4wk6o4b8d9fspf1i58o6ygn1gqu2mfzcycsb8vjf9hhlt59dm66kk7cnqunko7plxgzg8qgnqu44h0sj70ujucyl9t75cnwiptlcqq58tokx6p6xyzjgkdc3jr1op8rzujc5y8nr87dybp7is1iqtjtfs3devqanmh8v81cjrfk1nbfetd5ecu48ymr8ipe23kn3rjwmmi1fti8lo6jrwxebi3dy7sowofias68pbtvmhymvxo035w4t1r47ims54bnlx4k9hwftmj5c614e7fvlzsdwi3nzxh9nl5s37naoizt24oz0xrudpsnjqqjw0fbqarkjlia74mswg09kswxtp0i9el3rxclt7i2xkt7g65lo7aphgtau9pvho1ttlyph2suifmtb4tbgw26pqz408l654lzmq5leuocayxtvuwlwayq67q2zebrzkqhz67e9094o2jxtl6nfuimaewf1x6gwvc4mr2dof5yxtbau1ilj2mvt301nxd4z4tez5oli4xaxb4b4ae2h2tnqk2e3wzkwki79xddtiwk0dayk93ww1t0dkcnnaufnrw7fyumg5o6mkvtmj12t32j5s"
#wall = "2"
#shelf = "2"
#volume = "1"
#page = 153

#wholeBook = (pybel.getbook(hexName, wall, shelf, volume)).split("\n\n")
#print(f"\n{wholeBook[page-1]}\n")