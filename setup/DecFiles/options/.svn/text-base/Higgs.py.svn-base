from Configurables import Generation
from Gaudi.Configuration import *

Generation().PileUpTool = "FixedLuminosityForRareProcess"

importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

from Configurables import Special, PythiaProduction, Pythia8Production

Generation().addTool( Special )
Generation().Special.addTool( PythiaProduction )
Generation().Special.addTool( Pythia8Production )

Generation().Special.PythiaProduction.Commands += [
    "pysubs msel 0" , 
    "pysubs msub 24 1" ,
    "pysubs msub 26 1" ,
    "pypars mstp 128 0" ,
    "pydat3 mdme 174 1 0" ,
    "pydat3 mdme 175 1 0" ,
    "pydat3 mdme 176 1 0" ,
    "pydat3 mdme 177 1 0" ,
    "pydat3 mdme 178 1 0" ,
    "pydat3 mdme 179 1 0" ,
    "pydat3 mdme 180 1 0" ,
    "pydat3 mdme 181 1 0" ,
    "pydat3 mdme 182 1 1" ,
    "pydat3 mdme 183 1 0" ,
    "pydat3 mdme 184 1 1" ,
    "pydat3 mdme 185 1 0" ,
    "pydat3 mdme 186 1 0" ,
    "pydat3 mdme 187 1 0" ,
    "pydat3 mdme 188 1 0" ,
    "pydat3 mdme 189 1 0" ,
    "pydat3 mdme 190 1 0" ,
    "pydat3 mdme 191 1 0" ,
    "pydat3 mdme 192 1 0" ,
    "pydat3 mdme 193 1 0" ,
    "pydat3 mdme 194 1 0" ,
    "pydat3 mdme 195 1 0" ,
    "pydat3 mdme 196 1 0" ,
    "pydat3 mdme 197 1 0" ,
    "pydat3 mdme 198 1 0" ,
    "pydat3 mdme 199 1 0" ,
    "pydat3 mdme 200 1 0" ,
    "pydat3 mdme 201 1 0" ,
    "pydat3 mdme 202 1 0" ,
    "pydat3 mdme 203 1 0" ,
    "pydat3 mdme 204 1 0" ,
    "pydat3 mdme 205 1 0" ,
    "pydat3 mdme 206 1 1" ,
    "pydat3 mdme 207 1 1" ,
    "pydat3 mdme 208 1 0" ,
    "pydat3 mdme 209 1 0" ,
    "pydat3 mdme 210 1 0" ,
    "pydat3 mdme 211 1 0" ,
    "pydat3 mdme 212 1 0" ,
    "pydat3 mdme 213 1 0" ,
    "pydat3 mdme 214 1 1" ,
    "pydat3 mdme 215 1 0" ,
    "pydat3 mdme 216 1 0" ,
    "pydat3 mdme 217 1 0" ,
    "pydat3 mdme 218 1 0" ,
    "pydat3 mdme 219 1 0" ,
    "pydat3 mdme 220 1 0" ,
    "pydat3 mdme 221 1 0" ,
    "pydat3 mdme 222 1 0" ,
    "pydat3 mdme 223 1 0" ,
    "pydat3 mdme 224 1 0" ,
    "pydat3 mdme 225 1 0" ,
    "pydat3 mdme 226 1 0" ,
    "pydat3 mdme 227 1 0" ,
    "pydat3 mdme 228 1 0" ,
    "pydat3 mdme 229 1 0" ,
    "pydat3 mdme 230 1 0" ,
    "pydat3 mdme 231 1 0" ,
    "pydat3 mdme 232 1 0" ,
    "pydat3 mdme 233 1 0" ,
    "pydat3 mdme 234 1 0" ,
    "pydat3 mdme 235 1 0" ,
    "pydat3 mdme 236 1 0" ,
    "pydat3 mdme 237 1 0" ,
    "pydat3 mdme 238 1 0" ,
    "pydat3 mdme 239 1 0" ,
    "pydat3 mdme 240 1 0" ,
    "pydat3 mdme 241 1 0" ,
    "pydat3 mdme 242 1 0" ,
    "pydat3 mdme 243 1 0" ,
    "pydat3 mdme 244 1 0" ,
    "pydat3 mdme 245 1 0" ,
    "pydat3 mdme 246 1 0" ,
    "pydat3 mdme 247 1 0" ,
    "pydat3 mdme 248 1 0" ,
    "pydat3 mdme 249 1 0" ,
    "pydat3 mdme 250 1 0" ,
    "pydat3 mdme 251 1 0" ,
    "pydat3 mdme 252 1 0" ,
    "pydat3 mdme 253 1 0" ,
    "pydat3 mdme 254 1 0" ,
    "pydat3 mdme 255 1 0" ,
    "pydat3 mdme 256 1 0" ,
    "pydat3 mdme 257 1 0" ,
    "pydat3 mdme 258 1 0" ,
    "pydat3 mdme 259 1 0" ,
    "pydat3 mdme 260 1 0" ,
    "pydat3 mdme 261 1 0" ,
    "pydat3 mdme 262 1 0" ,
    "pydat3 mdme 263 1 0" ,
    "pydat3 mdme 264 1 0" ,
    "pydat3 mdme 265 1 0" ,
    "pydat3 mdme 266 1 0" ,
    "pydat3 mdme 267 1 0" ,
    "pydat3 mdme 268 1 0" ,
    "pydat3 mdme 269 1 0" ,
    "pydat3 mdme 270 1 0" ,
    "pydat3 mdme 271 1 0" ,
    "pydat3 mdme 272 1 0" ,
    "pydat3 mdme 273 1 0" ,
    "pydat3 mdme 274 1 0" ,
    "pydat3 mdme 275 1 0" ,
    "pydat3 mdme 276 1 0" ,
    "pydat3 mdme 277 1 0" ,
    "pydat3 mdme 278 1 0" ,
    "pydat3 mdme 279 1 0" ,
    "pydat3 mdme 280 1 0" ,
    "pydat3 mdme 281 1 0" ,
    "pydat3 mdme 282 1 0" ,
    "pydat3 mdme 283 1 0" ,
    "pydat3 mdme 284 1 0" ,
    "pydat3 mdme 285 1 0" ,
    "pydat3 mdme 286 1 0" ,
    "pydat3 mdme 287 1 0" ,
    "pydat3 mdme 288 1 0" 
]

#pythia8 production commands
Generation().Special.Pythia8Production.Commands += [
            "SpaceShower:rapidityOrder = off", #pT ordering!
            #"HiggsSM:gg2H = on", #Switch gg H_25 (H) production on
            "HiggsSM:ffbar2HZ  = on",
            "HiggsSM:ffbar2HW  = on",
            "25:onMode = off", #Turn H decays off
            "25:onIfAny = 5", #Turn on bbar decays
            "23:onMode = off", #Turn Z decays off
            "23:onIfAny = 13 11", #Turn on mu and e decays
            "24:onMode = off", #Turn W decays off
            "24:onIfAny = 13 11", #Turn on mu and e decays
            "PartonLevel:FSR=on" # FSR by PYTHIA8 (NOT PHOTOS)
            #Change of H_25 (H) mass is done in the dkfile
        ]
