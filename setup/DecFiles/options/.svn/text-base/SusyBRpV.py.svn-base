# Main configuration file to generate mSUGRA/AMSB with bilinear Rp violation
# @author Neal Gauvin (Gueissaz) 
# @date 10 july 2008
#

from Configurables import Generation
from Gaudi.Configuration import *

from Configurables import Special, PythiaProduction

Generation().addTool( Special )
Generation().Special.addTool( PythiaProduction )

Generation().Special.PythiaProduction.Commands += [ 
  #Set SUSY param
  "pymssm imss 1 11",  #Switch on SUSY MSSM input from an SLHA file.

  #light higgs production
  "pysubs msel 0 0",         #full user comtrol MSUB(ISUB)=1
  #"pysubs msel 39 1",         //Susy processes
  "pysubs msub 3 0",     #  fermion fusion
  "pysubs msub 24 0",     # ass. prod. with Vect bos.
  "pysubs msub 26 0",     # idem
  "pysubs msub 102 0",     # gluon fusion
  "pysubs msub 103 0",     # photon fusion
  "pysubs msub 111 0",     # gluon associated
  "pysubs msub 112 0",     # f associated
  "pysubs msub 113 0",     # g associated
  "pysubs msub 121 0",     # ass. prod with heavy fermions
  "pysubs msub 122 0",     # idem
  "pysubs msub 123 0",     # V. bos. fusion
  "pysubs msub 124 0",     # idem
  #BSM Neutral Higgs
  "pysubs msub 151 0",
  "pysubs msub 152 0",
  "pysubs msub 153 0",
  "pysubs msub 156 0",
  "pysubs msub 157 0",
  "pysubs msub 158 0",
  "pysubs msub 171 0",
  "pysubs msub 172 0",
  "pysubs msub 173 0",
  "pysubs msub 174 0",
  "pysubs msub 176 0",
  "pysubs msub 177 0",  # <---- vanishing cross-section
  "pysubs msub 178 0",  # <---- vanishing cross-section
  "pysubs msub 179 0",  # <---- vanishing cross-section
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

  #SUSY processes
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
  "pysubs msub 296 1"
]

#Set pythia parameters common to all susy models
importOptions( "$DECFILESROOT/options/Neutralino.py" )

