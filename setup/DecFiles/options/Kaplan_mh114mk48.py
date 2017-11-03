# Main configuration file to generate Susy decay acc. to Kaplan's model
# Generic Susy + h->kk, pile-up, at least 1 k in accept
# mk = 48GeV, mh = 114 GeV, k decays in the Velo (in luminous region)
# @author Neal Gauvin (Gueissaz) 
# @date 8 october 2008
#

#Provide a decay file to pythia
#Generation.Special.PythiaProduction.SLHADecayFile = "$DECFILESROOT/lha/Kaplan_hkk.LHdec";
#Generation.Special.PythiaProduction.PDecayList = { 1000022 };

from Configurables import Generation
from Gaudi.Configuration import *

from Configurables import Special, PythiaProduction

Generation().addTool( Special )
Generation().Special.addTool( PythiaProduction )

Generation().Special.PythiaProduction.Commands += [ 

  #Set SUSY param
  "pymssm imss 1 1",  #Switch on SUSY  MSSM input from hand

  #Set SUSY parameters for Kaplan model
  "pymssm rmss 1 63",    #M1
  "pymssm rmss 2 250",   #M2
  "pymssm rmss 4 140",   #mu
  "pymssm rmss 5 5.0",   #tanbeta
  "pymssm rmss 9 1000",  #right sqark
  "pymssm rmss 10 1000", #left sqark for third gener.
  "pymssm rmss 12 1000", #right stop mass
  "pymssm rmss 16 1000", #top trilinear coupling or common trilinear cplg A

  #light higgs production
  "pysubs msub 3 1",     #  fermion fusion
  "pysubs msub 24 1",     # ass. prod. with Vect bos.
  "pysubs msub 26 1",     # idem
  "pysubs msub 102 1",    # gluon fusion
  "pysubs msub 103 1",     # photon fusion vanishing sigma
  "pysubs msub 111 1",     # gluon associated
  "pysubs msub 112 1",     # f associated
  "pysubs msub 113 1",     # g associated
  "pysubs msub 121 1",     # ass. prod with heavy fermions
  "pysubs msub 122 1",     # idem
  "pysubs msub 123 1",     # V. bos. fusion
  "pysubs msub 124 1",     # idem

  #BSM Neutral Higgs (decay into susy part is not available)
  "pysubs msub 152 0",
  "pysubs msub 153 0", #vanishing sigma
  "pysubs msub 156 0",
  "pysubs msub 157 0",
  "pysubs msub 158 0", #vanishing sigma
  "pysubs msub 171 0",
  "pysubs msub 172 0",
  "pysubs msub 173 0",
  "pysubs msub 174 0",
  "pysubs msub 176 0",
  "pysubs msub 177 0",
  "pysubs msub 178 0",
  "pysubs msub 179 0",
  "pysubs msub 181 0",
  "pysubs msub 182 0",
  "pysubs msub 183 0",
  "pysubs msub 184 0",
  "pysubs msub 185 0",
  "pysubs msub 186 0",
  "pysubs msub 187 0",
  "pysubs msub 188 0",
  "pysubs msub 189 0",
  "pysubs msub 190 0",

  #Susy processes
  "pysubs msub 201 1",
  "pysubs msub 202 1",
  "pysubs msub 203 1",
  "pysubs msub 204 1",
  "pysubs msub 205 1",
  "pysubs msub 206 1",
  "pysubs msub 207 1",
  "pysubs msub 208 1",
  "pysubs msub 209 1",
  "pysubs msub 210 1",
  "pysubs msub 211 1",
  "pysubs msub 212 1",
  "pysubs msub 213 1",
  "pysubs msub 214 1",
  "pysubs msub 216 1",
  "pysubs msub 217 1",
  "pysubs msub 218 1",
  "pysubs msub 219 1",
  "pysubs msub 220 1",
  "pysubs msub 221 1",
  "pysubs msub 222 1",
  "pysubs msub 223 1",
  "pysubs msub 224 1",
  "pysubs msub 225 1",
  "pysubs msub 226 1",
  "pysubs msub 227 1",
  "pysubs msub 228 1",
  "pysubs msub 229 1",
  "pysubs msub 230 1",
  "pysubs msub 231 1",
  "pysubs msub 232 1",
  "pysubs msub 233 1",
  "pysubs msub 234 1",
  "pysubs msub 235 1",
  "pysubs msub 236 1",
  "pysubs msub 237 1",
  "pysubs msub 238 1",
  "pysubs msub 239 1",
  "pysubs msub 240 1",
  "pysubs msub 241 1",
  "pysubs msub 242 1",
  "pysubs msub 243 1",
  "pysubs msub 244 1",
  "pysubs msub 246 1",
  "pysubs msub 247 1",
  "pysubs msub 248 1",
  "pysubs msub 249 1",
  "pysubs msub 250 1",
  "pysubs msub 251 1",
  "pysubs msub 252 1",
  "pysubs msub 253 1",
  "pysubs msub 254 1",
  "pysubs msub 256 1",
  "pysubs msub 258 1",
  "pysubs msub 259 1",
  "pysubs msub 261 1",
  "pysubs msub 262 1",
  "pysubs msub 263 1",
  "pysubs msub 264 1",
  "pysubs msub 265 1",
  "pysubs msub 271 1",
  "pysubs msub 272 1",
  "pysubs msub 273 1",
  "pysubs msub 274 1",
  "pysubs msub 275 1",
  "pysubs msub 276 1",
  "pysubs msub 277 1",
  "pysubs msub 278 1",
  "pysubs msub 279 1",
  "pysubs msub 280 1",
  "pysubs msub 281 1",
  "pysubs msub 282 1",
  "pysubs msub 283 1",
  "pysubs msub 284 1",
  "pysubs msub 285 1",
  "pysubs msub 286 1",
  "pysubs msub 287 1",
  "pysubs msub 288 1",
  "pysubs msub 289 1",
  "pysubs msub 290 1",
  "pysubs msub 291 1",
  "pysubs msub 292 1",
  "pysubs msub 293 1",
  "pysubs msub 294 1",
  "pysubs msub 295 1",
  "pysubs msub 296 1",

  #higgs decay into neutralinos LSP  
  "pydat3 mdme 210 1 0",
  "pydat3 mdme 211 1 0",
  "pydat3 mdme 212 1 0",
  "pydat3 mdme 213 1 0",
  "pydat3 mdme 214 1 0",  #1
  "pydat3 mdme 215 1 0",
  "pydat3 mdme 216 1 -1",
  "pydat3 mdme 217 1 -1",
  "pydat3 mdme 218 1 0",
  "pydat3 mdme 219 1 0",
  "pydat3 mdme 220 1 0",
  "pydat3 mdme 221 1 -1",
  "pydat3 mdme 222 1 0",
  "pydat3 mdme 223 1 0",
  "pydat3 mdme 224 1 0",
  "pydat3 mdme 225 1 0",
  "pydat3 mdme 226 1 0",
  "pydat3 mdme 227 1 1",   #0
  "pydat3 mdme 228 1 0",
  "pydat3 mdme 229 1 0",
  "pydat3 mdme 230 1 0",
  "pydat3 mdme 231 1 0",
  "pydat3 mdme 232 1 0",
  "pydat3 mdme 233 1 0",
  "pydat3 mdme 234 1 0",
  "pydat3 mdme 235 1 0",
  "pydat3 mdme 236 1 0",
  "pydat3 mdme 237 1 0",
  "pydat3 mdme 238 1 0",
  "pydat3 mdme 239 1 0",
  "pydat3 mdme 240 1 0",
  "pydat3 mdme 241 1 0",
  "pydat3 mdme 242 1 0",
  "pydat3 mdme 243 1 0",
  "pydat3 mdme 244 1 0",
  "pydat3 mdme 245 1 0",
  "pydat3 mdme 246 1 0",
  "pydat3 mdme 247 1 0",
  "pydat3 mdme 248 1 0",
  "pydat3 mdme 249 1 0",
  "pydat3 mdme 250 1 0",
  "pydat3 mdme 251 1 0",
  "pydat3 mdme 252 1 0",
  "pydat3 mdme 253 1 0",
  "pydat3 mdme 254 1 0",
  "pydat3 mdme 255 1 0",
  "pydat3 mdme 256 1 0",
  "pydat3 mdme 257 1 0",
  "pydat3 mdme 258 1 0",
  "pydat3 mdme 259 1 0",
  "pydat3 mdme 260 1 0",
  "pydat3 mdme 261 1 0",
  "pydat3 mdme 262 1 0",
  "pydat3 mdme 263 1 0",
  "pydat3 mdme 264 1 0",
  "pydat3 mdme 265 1 0",
  "pydat3 mdme 266 1 0",
  "pydat3 mdme 267 1 0",
  "pydat3 mdme 268 1 0",
  "pydat3 mdme 269 1 0",
  "pydat3 mdme 270 1 0",
  "pydat3 mdme 271 1 0",
  "pydat3 mdme 272 1 0",
  "pydat3 mdme 273 1 0",
  "pydat3 mdme 274 1 0",
  "pydat3 mdme 275 1 0",
  "pydat3 mdme 276 1 0",
  "pydat3 mdme 277 1 0",
  "pydat3 mdme 278 1 0",
  "pydat3 mdme 279 1 0",
  "pydat3 mdme 280 1 0",
  "pydat3 mdme 281 1 0",
  "pydat3 mdme 282 1 0",
  "pydat3 mdme 283 1 0",
  "pydat3 mdme 284 1 0",
  "pydat3 mdme 285 1 0",
  "pydat3 mdme 286 1 0",
  "pydat3 mdme 287 1 0",
  "pydat3 mdme 288 1 0"
]
