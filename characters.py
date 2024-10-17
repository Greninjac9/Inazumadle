import flet as ft

Characters = [
    ### A ###
    
    { "Nombre": "ADÉ-KÉBÉ", "Curso": "2º", "Elemento": "Aire", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
    
    { "Nombre": "AIDEN-FROSTE", "Curso": "2º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF_ARES", "EQUIPO": "ALPINO_(ARES)" },
    
    { "Nombre": "AITOR-CAZADOR", "Curso": "1º", "Elemento": "Bosque", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
    
    { "Nombre": "ALAN-MASTER", "Curso": "1º", "Elemento": "Aire", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "NEO-JAPON" },

    { "Nombre": "AUSTIN-HOBBES", "Curso": "NINO", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FFI", "EQUIPO": "INAZUMA-JAPON" },
    
    { "Nombre": "AXEL-BLAZE_(ALEX-ZABEL)", "Curso": "ADULTO", "Elemento": "Fuego", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "MONTE-OLIMPO" },
    
    { "Nombre": "ALFA", "Curso": "Por_Definir", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG_ARM", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_1.0" },
    
    { "Nombre": "BYRON-LOVE_(APHRODITE)", "Curso": "2º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "KOR", "Debut": "FF", "EQUIPO": "ZEUS" },
    
    { "Nombre": "ARCHER-HAWKINS", "Curso": "2º", "Elemento": "Aire", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FFI", "EQUIPO": "INAZUMA-JAPON" },
    
    { "Nombre": "ARION-SHERWIND", "Curso": "1º", "Elemento": "Aire", "Posición": "MD",
      "Género": "M", "Invocador": "EG", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
    
    { "Nombre": "ARION-SHERWIND_(ARIONS)", "Curso": "1º", "Elemento": "Aire", "Posición": "DL",
      "Género": "M", "Invocador": "EG", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "LOS-ARIONS" },
    
    { "Nombre": "ARION SHERWIND_(CS)", "Curso": "1º", "Elemento": "Aire", "Posición": "MD",
      "Género": "M", "Invocador": "EG_ARM", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "CHRONO-STORM" },
    
    { "Nombre": "RAY-DARK_(ASTERO-BLACK)", "Curso": "ADULTO", "Elemento": "Montaña", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "GCG", "EQUIPO": "EARTH-ELEVEN" },
    
    { "Nombre": "AXEL-BLAZE", "Curso": "2º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },

    ### B ###
    
    { "Nombre": "BAI-LONG", "Curso": "1º", "Elemento": "Aire", "Posición": "DL",
      "Género": "M", "Invocador": "EG", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "EQUIPO-ZERO" },
    
    { "Nombre": "BAI-LONG_(CS)", "Curso": "1º", "Elemento": "Aire", "Posición": "DL",
      "Género": "M", "Invocador": "EG_ARM", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "CHRONO-STORM" },
    
    { "Nombre": "BAI-LONG_(RESISTENCIA)", "Curso": "1º", "Elemento": "Aire", "Posición": "DL",
      "Género": "M", "Invocador": "EG", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "NEO-JAPON_(RESISTENCIA-DE-JAPON)" },
    
    { "Nombre": "BELLATRIX", "Curso": "2º", "Elemento": "Aire", "Posición": "MD",
      "Género": "F", "Invocador": "EG-N", "Nacionalidad": "Por_Definir", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS (GENESIS)" },
    
    { "Nombre": "BETA", "Curso": "Por_Definir", "Elemento": "Aire", "Posición": "DL",
      "Género": "F", "Invocador": "EG_ARM", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_2.0" },
    
    { "Nombre": "BOBBY-SHEARER", "Curso": "2º", "Elemento": "Bosque", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "EEUU", "Debut": "FF", "EQUIPO": "RAIMON" },
    
    { "Nombre": "BOBBY-SHEARER_(UNICORN)", "Curso": "2º", "Elemento": "Bosque", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "EEUU", "Debut": "FF", "EQUIPO": "UNICORN" },
    
    { "Nombre": "BRIAR-BLOOMHURST", "Curso": "2º", "Elemento": "Montaña", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF_VR", "EQUIPO": "SOUTH-CIRRUS" },
    
    { "Nombre": "BRYCE-WITHINGALE", "Curso": "2º", "Elemento": "Aire", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "KOR", "Debut": "FFI", "EQUIPO": "DRAGONES-DE-FUEGO" },
    
    { "Nombre": "BUDDY-FURY", "Curso": "3º", "Elemento": "Montaña", "Posición": "MD",
      "Género": "M", "Invocador": "Totem", "Nacionalidad": "JAP", "Debut": "GCG", "EQUIPO": "EARTH-ELEVEN" },
    
    { "Nombre": "BUNNY-COTTONTAIL", "Curso": "1º", "Elemento": "Aire", "Posición": "DL",
      "Género": "F", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF_ARES", "EQUIPO": "ALPINO_(ARES)" },
    
    { "Nombre": "BYRON-LOVE", "Curso": "2º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "KOR", "Debut": "FF", "EQUIPO": "DRAGONES-DE-FUEGO" },

    ### C ###
    
    { "Nombre": "CALEB-STONEWALL", "Curso": "2º", "Elemento": "Fuego", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "INAZUMA-JAPON" },
    
    { "Nombre": "CALEB-STONEWALL_(ADULTO)", "Curso": "ADULTO", "Elemento": "Fuego", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "NEO-JAPON_(RESISTENCIA-DE-JAPON)" },
    
    { "Nombre": "CALEB-STONEWALL_(REDUX)", "Curso": "2º", "Elemento": "Fuego", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(REDUX)" },
    
    { "Nombre": "CELIA-HILLS", "Curso": "1º", "Elemento": "Aire", "Posición": "MD",
      "Género": "F", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "EQUIPO-FEMENINO" },
    
    { "Nombre": "CERISE-BLOSSOM", "Curso": "2º", "Elemento": "Aire", "Posición": "MD",
      "Género": "F", "Invocador": "Totem", "Nacionalidad": "JAP", "Debut": "GCG", "EQUIPO": "EARTH-ELEVEN" },
      
    { "Nombre": "CLAUDE-BEACONS", "Curso": "2º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "KOR", "Debut": "FFI", "EQUIPO": "DRAGONES-DE-FUEGO" },
        
    { "Nombre": "CRONUS-FOURSEASONS", "Curso": "2º", "Elemento": "Fuego", "Posición": "MD",
      "Género": "M", "Invocador": "EG", "EQUIPO": "MONTE-OLIMPO" },
    
    { "Nombre": "CRONUS-FOURSEASONS_(RESISTENCIA)", "Curso": "2º", "Elemento": "Fuego", "Posición": "MD",
      "Género": "M", "Invocador": "EG", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "NEO-JAPON_(RESISTENCIA-DE-JAPON)" },
    
    ### D ###
    
    { "Nombre": "DARREN-LACHANCE", "Curso": "1º", "Elemento": "Bosque", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "RAIMON_II" },
      
    { "Nombre": "DAVE-QUAGMIRE", "Curso": "3º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "NEO-JAPON" },
        
    { "Nombre": "DAVID-SAMFORD", "Curso": "2º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "INAZUMA-JAPON" },
      
    { "Nombre": "DAVID-SAMFORD_(LEGENDARIO)", "Curso": "ADULTO", "Elemento": "Bosque", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "INAZUMA-JAPON_LEGENDARIO" },
      
    { "Nombre": "DAVID-SAMFORD_(REDUX)", "Curso": "2º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ACADEMIA-ALIUS (REDUX)" },
      
    { "Nombre": "DAVY-JONES", "Curso": "2º", "Elemento": "Aire", "Posición": "DL",
      "Género": "M", "Invocador": "EG", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "NEO-JAPON_(RESISTENCIA-DE-JAPON)" },
      
    { "Nombre": "DESTIN-BILLOWS", "Curso": "1º", "Elemento": "Bosque", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF_VR", "EQUIPO": "SOUTH-CIRRUS" },
      
    { "Nombre": "DAVE-QUAGMIRE_(DVALIN)", "Curso": "3º", "Elemento": "Fuego", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(EPSILON)" },

    ### E ###

    { "Nombre": "ELLIOT-EMBER_(ORION)", "Curso": "1º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF_ARES", "EQUIPO": "INAZUMA-JAPON_(ORION)" },
      
    { "Nombre": "ERIK-EAGLE", "Curso": "2º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "EEUU", "Debut": "FF", "EQUIPO": "RAIMON" },
      
    { "Nombre": "ERIK-EAGLE_(UNICORN)", "Curso": "2º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "EEUU", "Debut": "FF", "EQUIPO": "UNICORN" },
      
    { "Nombre": "EUGENE-PEABODY", "Curso": "2º", "Elemento": "Aire", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },

    ### F ###
    
    { "Nombre": "FALCO-FLASHMAN", "Curso": "2º", "Elemento": "Aire", "Posición": "DL",
      "Género": "M", "Invocador": "Totem", "Nacionalidad": "JAP", "Debut": "GCG", "EQUIPO": "EARTH-ELEVEN" },
      
    { "Nombre": "FEI-RUNE", "Curso": "Por_Definir", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "LOS-ARIONS" },
      
    { "Nombre": "FEI-RUNE_(CS)", "Curso": "Por_Definir", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG_ARM", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "CHRONO_STORM" },
      
    { "Nombre": "FLORA", "Curso": "Por_Definir", "Elemento": "Aire", "Posición": "DL",
      "Género": "F", "Invocador": "EG_ARM", "Nacionalidad": "Por_definir", "Debut": "Por_definir", "EQUIPO": "DESESPERDIDOS" },
      
    { "Nombre": "FRANK-FOREMAN", "Curso": "2º", "Elemento": "Fuego", "Posición": "DF",
      "Género": "M", "Invocador": "Totem", "Nacionalidad": "JAP", "Debut": "GCG", "EQUIPO": "EARTH-ELEVEN" },
    
    ### G ###

    { "Nombre": "GABRIEL-GARCÍA", "Curso": "2º", "Elemento": "Bosque", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "GABRIEL-GARCÍA_(CS)", "Curso": "2º", "Elemento": "Bosque", "Posición": "DF",
      "Género": "M", "Invocador": "EG_ARM", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "CHRONO-STORM" },
      
    { "Nombre": "GAMMA", "Curso": "Por_Definir", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG_ARM", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_3.0" },
      
    { "Nombre": "BRYCE-WITHINGALE_()", "Curso": "2º", "Elemento": "Aire", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "KOR", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(CAOS)" },
      
    { "Nombre": "GOLDIE-LEMMON_(CS)", "Curso": "1º", "Elemento": "Fuego", "Posición": "DF",
      "Género": "F", "Invocador": "EG_ARM", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "CHRONO-STORM" },   

    ### H ###

    { "Nombre": "HARROLD-HOUDINI_(RESISTENCIA)", "Curso": "3º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "NEO-JAPON_(RESISTENCIA-DE-JAPON)" },
      
    { "Nombre": "HECTOR-HELIO", "Curso": "2º", "Elemento": "Fuego", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "COS", "Debut": "FFI", "EQUIPO": "THE-LITTLE-GIANTS" },
      
    { "Nombre": "HOTEL", "Curso": "Por_Definir", "Elemento": "Montaña", "Posición": "PR",
      "Género": "M", "Invocador": "EG", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_1.0" },
      
    { "Nombre": "HUGUES-BAUDET", "Curso": "2º", "Elemento": "Aire", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "XAVIER-FOSTER_(HUNTER)", "Curso": "3º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF_ARES", "EQUIPO": "ACADEMIA-ALIA" },

    { "Nombre": "XAVIER-FOSTER_(HUNTER_ORION)", "Curso": "3º", "Elemento": "Fuego", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF_ARES", "EQUIPO": "INAZUMA-JAPON_(ORION)" },
      
    { "Nombre": "HURLEY-KANE", "Curso": "3º", "Elemento": "Aire", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "RAIMON_II" },
      
    ### I ### 
    ### J ###
    
    { "Nombre": "JACK-WALLSIDE", "Curso": "1º", "Elemento": "Montaña", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },
      
    { "Nombre": "JORDAN-GREENWAY_(JANUS)", "Curso": "2º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(TORMENTA-DE-GEMINIS)" },
      
    { "Nombre": "JEAN-PIERRE-LAPAN", "Curso": "1º", "Elemento": "Montaña", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "JEAN-PIERRE-LAPAN_(CS)", "Curso": "1º", "Elemento": "Montaña", "Posición": "PR",
      "Género": "M", "Invocador": "EG_ARM", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "CHRONO-STORM" },

    { "Nombre": "JIM-WRAITH", "Curso": "2º", "Elemento": "Bosque", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },
      
    { "Nombre": "JUDE-SHARP", "Curso": "2º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },
      
    { "Nombre": "JOSEPH-KING", "Curso": "2º", "Elemento": "Fuego", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "NEO-JAPON" },
      
    { "Nombre": "JOSEPH-KING_(REDUX)", "Curso": "2º", "Elemento": "Fuego", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ACADEMIA-ALIUS_(REDUX)" },
      
    { "Nombre": "JORDAN-GREENWAY", "Curso": "2º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FFI", "EQUIPO": "INAZUMA-JAPON" },
      
    { "Nombre": "JULIETA", "Curso": "Por_Definir", "Elemento": "Bosque", "Posición": "DL",
      "Género": "F", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_1.0" },
      
    ### K ###

    { "Nombre": "KEENAN-SHARPE", "Curso": "1º", "Elemento": "Montaña", "Posición": "DF",
      "Género": "M", "Invocador": "Totem", "Nacionalidad": "JAP", "Debut": "GCG", "EQUIPO": "EARTH-ELEVEN" },
      
    { "Nombre": "KEVIN-DRAGONFLY", "Curso": "2º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },
      
    { "Nombre": "KEVIN-DRAGONFLY (ARES)", "Curso": "3º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ALPINO_(ARES)" },  

    ### L ###

    { "Nombre": "LUCIAN-DARK", "Curso": "1º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
       
    ### M ###
    
    { "Nombre": "MARK-EVANS", "Curso": "2º", "Elemento": "Montaña", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },
      
    { "Nombre": "MARK-EVANS_(II)", "Curso": "2º", "Elemento": "Montaña", "Posición": "DF_LB",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON_II" },
      
    { "Nombre": "MARK-EVANS_(ADULTO)", "Curso": "ADULTO", "Elemento": "Montaña", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "MARK-EVANS_(ARIONS)", "Curso": "2º", "Elemento": "Montaña", "Posición": "PR",
      "Género": "M", "Invocador": "EG", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "LOS-ARIONS" },
      
    { "Nombre": "MARK-EVANS_(LEGENDARIO)", "Curso": "ADULTO", "Elemento": "Montaña", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "INAZUMA-JAPON_LEGENDARIO" },
      
    { "Nombre": "MAXWELL-CARSON", "Curso": "2º", "Elemento": "Aire", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },
      
    { "Nombre": "MARK-EVANS_(MECHAMARK)", "Curso": "Por_Definir", "Elemento": "Montaña", "Posición": "PR",
      "Género": "M", "Invocador": "EG", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_(EL-DORADO-02)" },
      
    { "Nombre": "MICHAEL-BALLZACK", "Curso": "2º", "Elemento": "Montaña", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "MIKE", "Curso": "Por_Definir", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_1.0" },
      
    { "Nombre": "RAY-DARK_(MISTER-D)", "Curso": "ADULTO", "Elemento": "Montaña", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ORFEO" },   

    ### N ###
    
    { "Nombre": "NATHAN-SWIFT", "Curso": "2º", "Elemento": "Aire", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },
      
    { "Nombre": "NELLY-RAIMON", "Curso": "2º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "F", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "EQUIPO-FEMENINO" },
      
    { "Nombre": "NIGEL-AUGUST_(NEPPTEN)", "Curso": "2º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(CAOS)" },
      
    { "Nombre": "NJORD-SNIO", "Curso": "2º", "Elemento": "Aire", "Posición": "DL",
      "Género": "M", "Invocador": "EG", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "ALPINO_(GO)" },
      
    { "Nombre": "NJORD-SNIO_(RESISTENCIA)", "Curso": "2º", "Elemento": "Aire", "Posición": "DL",
      "Género": "M", "Invocador": "EG", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "NEO-JAPON_(RESISTENCIA-DE-JAPON)" },    

    ### O ###
    ### P ###
    
    { "Nombre": "PAOLO-BIANCHI", "Curso": "2º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "ITA", "Debut": "FFI", "EQUIPO": "ORFEO" },
      
    { "Nombre": "PERCIVAL-TRAVIS", "Curso": "ADULTO", "Elemento": "Bosque", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FFI", "EQUIPO": "INAZUMA-JAPON" },
      
    { "Nombre": "PERCY-HURST_(PERSEO)", "Curso": "2º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF_ARES", "EQUIPO": "ZEUS_(ARES)" },
      
    ### Q ###

    { "Nombre": "QUENTIN-CINQUEDEA_(RESISTENCIA)", "Curso": "2º", "Elemento": "Fuego", "Posición": "PR",
      "Género": "M", "Invocador": "EG", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "NEO-JAPON_(RESISTENCIA-DE-JAPON)" },    
    
    ### R ###
    
    { "Nombre": "RAY-DARK", "Curso": "ADULTO", "Elemento": "Montaña", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ACADEMIA-ALIUS_(REDUX)" },
      
    { "Nombre": "RICCARDO-DI-RIGO", "Curso": "2º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "RICCARDO-DI-RIGO_(CS)", "Curso": "2º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG_ARM", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "CHRONO-STORM" },
      
    { "Nombre": "RYOMA-NISHIKI", "Curso": "2º", "Elemento": "Montaña", "Posición": "MD",
      "Género": "M", "Invocador": "EG", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "RYOMA-NISHIKI_(CS)", "Curso": "2º", "Elemento": "Montaña", "Posición": "MD",
      "Género": "M", "Invocador": "EG_ARM", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "CHRONO-STORM" }, 

    ### S ###
    
    { "Nombre": "SAM-KINCAID", "Curso": "1º", "Elemento": "Fuego", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },
      
    { "Nombre": "SAMGUK-HAN", "Curso": "3º", "Elemento": "Fuego", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "SEYMOUR-HILLMAN", "Curso": "ADULTO", "Elemento": "Montaña", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },
      
    { "Nombre": "SCOTT-BANYAN", "Curso": "1º", "Elemento": "Bosque", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "RAIMON_II" },
      
    { "Nombre": "SHAWN-FROSTE", "Curso": "2º", "Elemento": "Aire", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "INAZUMA-JAPON" },
      
    { "Nombre": "SHAWN-FROSTE_(ADULTO)", "Curso": "ADULTO", "Elemento": "Aire", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ALPINO_(GO)" },
      
    { "Nombre": "SHAWN-FROSTE_(AIDEN)", "Curso": "2º", "Elemento": "Aire", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "RAIMON_II" },
      
    { "Nombre": "SHAWN-FROSTE_(DF)", "Curso": "2º", "Elemento": "Aire", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "RAIMON_II" },
      
    { "Nombre": "SHAWN-FROSTE_(LEGENDARIO)", "Curso": "ADULTO", "Elemento": "Aire", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "INAZUMA-JAPON_LEGENDARIO" },
      
    { "Nombre": "SHAWN-FROSTE_(ORION)", "Curso": "3º", "Elemento": "Aire", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF_ARES", "EQUIPO": "INAZUMA-JAPON_(ORION)" },
      
    { "Nombre": "SHUNSUKE-AOYAMA", "Curso": "2º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "SILVIA-WOODS", "Curso": "2º", "Elemento": "Montaña", "Posición": "PR",
      "Género": "F", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "EQUIPO-FEMENINO" },
      
    { "Nombre": "SOL-DAYSTAR_(CS)", "Curso": "1º", "Elemento": "Fuego", "Posición": "MD",
      "Género": "M", "Invocador": "EG_ARM", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "CHRONO-STORM" },
      
    { "Nombre": "SOR_(CS)", "Curso": "Por_Definir", "Elemento": "Aire", "Posición": "DF",
      "Género": "M", "Invocador": "EG_ARM", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "CHRONO-STORM" },
      
    { "Nombre": "STEVE-GRIM", "Curso": "2º", "Elemento": "Aire", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },
      
    { "Nombre": "SUBARU-HONDA", "Curso": "3º", "Elemento": "Fuego", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "SUZETTE-HARTLAND", "Curso": "2º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "F", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "RAIMON_II" },
      
    ### T ###

    { "Nombre": "TERRY-ARCHIBALD", "Curso": "2º", "Elemento": "Aire", "Posición": "PR",
      "Género": "M", "Invocador": "Totem", "Nacionalidad": "JAP", "Debut": "GCG", "EQUIPO": "EARTH-ELEVEN" },
      
    { "Nombre": "TEZCAT", "Curso": "1º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "EQUIPO-ZERO" },

    { "Nombre": "TIM-SAUNDERS", "Curso": "1º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },
      
    { "Nombre": "TOD-IRONSIDE", "Curso": "1º", "Elemento": "Fuego", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },
      
    { "Nombre": "CLAUDE-BEACONS_(TORCH)", "Curso": "2º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "KOR", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(CAOS)" },
      
    { "Nombre": "VICTORIA-VANGUARD", "Curso": "2º", "Elemento": "Aire", "Posición": "MD",
      "Género": "F", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "RAIMON_II" },
      
    { "Nombre": "TRINA-VERDURE", "Curso": "1º", "Elemento": "Bosque", "Posición": "DF",
      "Género": "F", "Invocador": "Totem", "Nacionalidad": "JAP", "Debut": "GCG", "EQUIPO": "EARTH-ELEVEN" },
      
    { "Nombre": "TYLER-MURDOCK", "Curso": "2º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "NEO-JAPON" },
      
    ### U ###
    ### V ###

    { "Nombre": "VICTOR-BLADE", "Curso": "1º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "VICTOR-BLADE_(CS)", "Curso": "1º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG_ARM", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "CHRONO-STORM" },
      
    { "Nombre": "VLADIMIR-BLADE", "Curso": "ADULTO", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG_ARM", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "LOS-ARIONS" },
      
    ### W ###

    { "Nombre": "WANLI-CHANGCHENG", "Curso": "3º", "Elemento": "Montaña", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "WILLIAM-GLASS", "Curso": "2º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },

    ### X ###
    
    { "Nombre": "XAVIER-FOSTER", "Curso": "2º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FFI", "EQUIPO": "INAZUMA-JAPON" },
      
    { "Nombre": "XAVIER-FOSTER_(SCHILLER)", "Curso": "ADULTO", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FFI", "EQUIPO": "INAZUMA-JAPON_LEGENDARIO" },
      
    { "Nombre": "XAVIER-SCHILLER", "Curso": "2º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N",  "Nacionalidad": "JAP", "Debut": "FF_ARES", "EQUIPO": "ACADEMIA-ALIA" },
      
    { "Nombre": "XAVIER-FOSTER_(XENE)", "Curso": "2º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(GENESIS)" },
      
    ### Y ###
    ### Z ###

    { "Nombre": "ZACK-AVALON", "Curso": "3º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "Totem", "Nacionalidad": "JAP", "Debut": "GCG", "EQUIPO": "EARTH-ELEVEN" },
      
    { "Nombre": "ZANARK-AVALONIC_(CS)", "Curso": "Por_Definir", "Elemento": "Montaña", "Posición": "DL",
      "Género": "M", "Invocador": "EG_ARM", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "CHRONO-STORM" },
      
    { "Nombre": "ZIPPY-LERNER", "Curso": "1º", "Elemento": "Aire", "Posición": "DF",
      "Género": "M", "Invocador": "Totem", "Nacionalidad": "JAP", "Debut": "GCG", "EQUIPO": "EARTH-ELEVEN"}     
]

CharacterRef = [
    ### A ###
    'Adé Kébé', 'Aiden Froste', 'Aitor Cazador', 'Alan Master', 'Austin Hobbes', 'Alex Zabel', 'Alfa', 'Aphrodite', 'Archer Hawkins', 
    'Arion Sherwind', 'Arion Sherwind (Arions)', 'Arion Sherwind (Chrono Stones)', 
    'Astero Black', 'Axel Blaze', 
    ### B ### 
    'Bai Long', 'Bai Long (Chrono Stones)', 'Bai Long (Resistencia)', 'Bellatrix', 'Beta', 'Bobby Shearer', 'Bobby Shearer (Unicorn)',
    'Briar Bloomhurst', 'Bryce Withingale', 'Buddy Fury', 'Bunny Cottontail', 'Byron Love', 
    ### C ###
    'Caleb Stonewall', 'Caleb Stonewall (Adulto)', 'Caleb Stonewall (Redux)', 'Celia Hills', 
    'Cerise Blossom', 'Claude Beacons', 'Cronus Fourseasons', 'Cronus Fourseasons (Resistencia)',
    ### D ###
    'Darren Lachance', 'Dave Quagmire', 'David Samford', 'David Samford (Legendario)',
    'David Samford (Redux)', 'Davy Jones','Destin Billows','Dvalin',
    ### E ###
    'Elliot Ember (Orion)', 'Erik Eagle', 'Erik Eagle (Unicorn)', 'Eugene Peabody', 
    ### F ###
    'Falco Flashman', 'Fei Rune', 'Fei Rune (Chrono Stones)', 'Flora', 'Frank Foreman',
    ### G ###
    'Gabriel García', 'Gabriel García (Chrono Stones)', 'Gamma', 'Gazelle', 'Goldie Lemmon (Chrono Stones)', 
    ### H ###
    'Harrold Houdini (Resistencia)', 'Hector Helio', 'Hotel', 'Hugh', 
    'Hunter Foster', 'Hunter Foster (Orion)', 'Hurley Kane', 
    ### J ###
    'Jack Wallside', 'Janus', 'Jean-Pierre Lapan', 'Jean-Pierre Lapan (Chrono Stones)', 'Jim Wraith', 'Jude Sharp', 
    'Joseph King', 'Joseph King (Redux)', 'Jordan Greenway', 'Julieta', 
    ### K ###
    'Keenan Sharpe', 'Kevin Dragonfly', 'Kevin Dragonfly (Ares)',
    ### L ###
    'Lucian Dark', 
    ### M ###
    'Mark Evans', 'Mark Evans (II)', 'Mark Evans (Adulto)', 'Mark Evans (Arions)', 'Mark Evans (Legendario)', 
    'Max', 'Mechamark', 'Michael Ballzack', 'Mike', 'Mister D', 
    ### N ###
    'Nathan Swift', 'Nelly Raimon', 'Neppten', 'Njord Snio', 'Njord Snio (Resistencia)',
    ### O ###
    ### P ###
    'Paolo Bianchi', 'Percival Travis', 'Perseo',
    ### Q ###
    'Quentin Cinquedea (Resistencia)',
    ### R ###
    'Ray Dark', 'Riccardo Di Rigo', 'Riccardo Di Rigo (Chrono Stones)', 'Ryoma Nishiki', 'Ryoma Nishiki (Chrono Stones)', 
    ### S ###
    'Sam Kincaid', 'Samguk Han', 'Seymour Hillman', 'Scotty', 'Shawn Froste (Unido)', 'Shawn Froste (Adulto)', 'Shawn Froste (Aiden)', 
    'Shawn Froste (DF)', 'Shawn Froste (Legendario)', 'Shawn Froste (Orion)', 'Shun', 'Silvia Woods', 'Sol Daystar (Chrono Stones)', 
    'Sor (Chrono Stones)', 'Steve Grim', 'Subaru Honda', 'Sue', 
    ### T ###
    'Terry Archibald', 'Tezcat', 'Timmy', 'Tod Ironside', 'Torch', 'Tori', 'Trina Verdure', 'Tyler Murdock', 
    ### V ###
    'Victor Blade', 'Victor Blade (Chrono Stones)', 'Vladimir Blade', 
    ### W ###
    'Wanli Changcheng', 'William Glass',
    ### X ###
    'Xavier Foster', 'Xavier Schiller', 'Xavier Schiller (Ares)', 'Xene', 
    ### Y ###
    ### Z ###
    'Zack Avalon', 'Zanark Avalonic (Chrono Stones)', 'Zippy Lerner'
]

Table = ft.Row(
          alignment=ft.MainAxisAlignment.CENTER,
          spacing = 15,
          controls=[
              ft.Container(
                  content=ft.Text("Jugador", weight=ft.FontWeight.BOLD),
                  border = ft.border.all(5, ft.colors.GREY_300),
                  height = 30, width = 80,
                  bgcolor=ft.colors.GREY_300, border_radius = 10,
                  alignment=ft.alignment.center
              ),
              ft.Container(
                  content=ft.Text("Curso", weight=ft.FontWeight.BOLD),
                  border = ft.border.all(5, ft.colors.GREY_300),
                  height = 30, width = 80,
                  bgcolor=ft.colors.GREY_300, border_radius = 10,
                  alignment=ft.alignment.center
              ),
              ft.Container(
                  content=ft.Text("Elemento", weight=ft.FontWeight.BOLD),
                  border = ft.border.all(5, ft.colors.GREY_300),
                  height = 30, width = 80,
                  bgcolor=ft.colors.GREY_300, border_radius = 10,
                  alignment=ft.alignment.center
              ),
              ft.Container(
                  content=ft.Text("Posición", weight=ft.FontWeight.BOLD),
                  border = ft.border.all(5, ft.colors.GREY_300),
                  height = 30, width = 80,
                  bgcolor=ft.colors.GREY_300, border_radius = 10,
                  alignment=ft.alignment.center
              ),
              ft.Container(
                  content=ft.Text("Género", weight=ft.FontWeight.BOLD),
                  border = ft.border.all(5, ft.colors.GREY_300),
                  height = 30, width = 80,
                  bgcolor=ft.colors.GREY_300, border_radius = 10,
                  alignment=ft.alignment.center
              ),
              ft.Container(
                  content=ft.Text("Invocador", weight=ft.FontWeight.BOLD),
                  border = ft.border.all(5, ft.colors.GREY_300),
                  height = 30, width = 80,
                  bgcolor=ft.colors.GREY_300, border_radius = 10,
                  alignment=ft.alignment.center
              ),
              ft.Container(
                  content=ft.Text("Nación", weight=ft.FontWeight.BOLD),
                  border = ft.border.all(5, ft.colors.GREY_300),
                  height = 30, width = 80,
                  bgcolor=ft.colors.GREY_300, border_radius = 10,
                  alignment=ft.alignment.center
              ),
              ft.Container(
                  content=ft.Text("Debut", weight=ft.FontWeight.BOLD),
                  border = ft.border.all(5, ft.colors.GREY_300),
                  height = 30, width = 80,
                  bgcolor=ft.colors.GREY_300, border_radius = 10,
                  alignment=ft.alignment.center
              ),
              ft.Container(
                  content=ft.Text("Equipo", weight=ft.FontWeight.BOLD),
                  border = ft.border.all(5, ft.colors.GREY_300),
                  height = 30, width = 80,
                  bgcolor=ft.colors.GREY_300, border_radius = 10,
                  alignment=ft.alignment.center
              ),])
