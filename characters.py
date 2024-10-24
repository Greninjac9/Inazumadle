import flet as ft

Characters = [
    ### A ###
    
    { "Nombre": "ADÉ-KÉBÉ", "Curso": "2º", "Elemento": "Aire", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "6", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
    
    { "Nombre": "AIDEN-FROSTE", "Curso": "2º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Nacionalidad": "JAP", "Debut": "FF_ARES", "EQUIPO": "ALPINO_(ARES)" },
    
    { "Nombre": "AITOR-CAZADOR", "Curso": "1º", "Elemento": "Bosque", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "15", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },

    { "Nombre": "ALAN-MASTER", "Curso": "1º", "Elemento": "Aire", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "4", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ROYAL-ACADEMY" },
    
    { "Nombre": "ALAN-MASTER_(NEO)", "Curso": "1º", "Elemento": "Aire", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "2", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "NEO-JAPON" },

    { "Nombre": "AQUILINA SCHILLER", "Curso": "ADULTO", "Elemento": "Bosque", "Posición": "DT",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "-", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "RAIMON_II" },

    { "Nombre": "LANE-WAR_ARES", "Curso": "1º", "Elemento": "Aire", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "4", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "NEO-JAPON" },
    
    { "Nombre": "ARTIE-MISHMAN_ARTEMIS", "Curso": "2º", "Elemento": "Aire", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "6", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ZEUS" },
    
    { "Nombre": "AUSTIN-HOBBES", "Curso": "NINO", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Nacionalidad": "JAP", "Debut": "FFI", "EQUIPO": "INAZUMA-JAPON" },
    
    { "Nombre": "AXEL-BLAZE_(ALEX-ZABEL)", "Curso": "ADULTO", "Elemento": "Fuego", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "MONTE-OLIMPO" },
    
    { "Nombre": "ALFA", "Curso": "Por_Definir", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "10",  "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_1.0" },
    
    { "Nombre": "BYRON-LOVE_(APHRODITE)", "Curso": "2º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10",  "Nacionalidad": "KOR", "Debut": "FF", "EQUIPO": "ZEUS" },

    { "Nombre": "APOLLO-LIGHT_APOLLO", "Curso": "2º", "Elemento": "Bosque", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "2",  "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ZEUS" },
    
    { "Nombre": "ARCHER-HAWKINS", "Curso": "2º", "Elemento": "Aire", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "7",  "Nacionalidad": "JAP", "Debut": "FFI", "EQUIPO": "INAZUMA-JAPON" },
    
    { "Nombre": "ARION-SHERWIND", "Curso": "1º", "Elemento": "Aire", "Posición": "MD",
      "Género": "M", "Invocador": "EG", "Dorsal": "8", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
    
    { "Nombre": "ARION-SHERWIND_(ARIONS)", "Curso": "1º", "Elemento": "Aire", "Posición": "DL",
      "Género": "M", "Invocador": "EG", "Dorsal": "8",  "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "LOS-ARIONS" },
    
    { "Nombre": "ARION-SHERWIND_(CS)", "Curso": "1º", "Elemento": "Aire", "Posición": "MD",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "8",  "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "CHRONO-STORM" },
    
    { "Nombre": "RAY-DARK_(ASTERO-BLACK)", "Curso": "ADULTO", "Elemento": "Montaña", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-",  "Nacionalidad": "JAP", "Debut": "GCG", "EQUIPO": "EARTH-ELEVEN" },

    { "Nombre": "WESLEY-KNOX_ATHENA", "Curso": "1º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "8",  "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ZEUS" },
    
    { "Nombre": "AXEL-BLAZE", "Curso": "2º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10",  "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },

    ### B ###
    
    { "Nombre": "BAI-LONG", "Curso": "1º", "Elemento": "Aire", "Posición": "DL",
      "Género": "M", "Invocador": "EG", "Dorsal": "10",  "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "EQUIPO-ZERO" },
    
    { "Nombre": "BAI-LONG_(CS)", "Curso": "1º", "Elemento": "Aire", "Posición": "DL",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "19",  "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "CHRONO-STORM" },
    
    { "Nombre": "BAI-LONG_(RESISTENCIA)", "Curso": "1º", "Elemento": "Aire", "Posición": "DL",
      "Género": "M", "Invocador": "EG", "Dorsal": "10",  "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "NEO-JAPON_(RESISTENCIA-DE-JAPON)" },
    
    { "Nombre": "BELLATRIX", "Curso": "2º", "Elemento": "Aire", "Posición": "MD",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "10",  "Nacionalidad": "Por_Definir", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS (GENESIS)" },
    
    { "Nombre": "BETA", "Curso": "Por_Definir", "Elemento": "Aire", "Posición": "DL",
      "Género": "F", "Invocador": "EG_ARM", "Dorsal": "10",  "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_2.0" },

    { "Nombre": "BEN-SIMMONS", "Curso": "2º", "Elemento": "Bosque", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "3",  "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ROYAL-ACADEMY" },
    
    { "Nombre": "BOBBY-SHEARER", "Curso": "2º", "Elemento": "Bosque", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "13",  "Nacionalidad": "EEUU", "Debut": "FF", "EQUIPO": "RAIMON" },

    { "Nombre": "BOBBY-SHEARER_II", "Curso": "2º", "Elemento": "Bosque", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "13",  "Nacionalidad": "EEUU", "Debut": "FF", "EQUIPO": "RAIMON_II" },
    
    { "Nombre": "BOBBY-SHEARER_(UNICORN)", "Curso": "2º", "Elemento": "Bosque", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "5", "Nacionalidad": "EEUU", "Debut": "FF", "EQUIPO": "UNICORN" },
    
    { "Nombre": "BRIAR-BLOOMHURST", "Curso": "2º", "Elemento": "Montaña", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Nacionalidad": "JAP", "Debut": "FF_VR", "EQUIPO": "SOUTH-CIRRUS" },
    
    { "Nombre": "BRYCE-WHITINGALE", "Curso": "2º", "Elemento": "Aire", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Nacionalidad": "KOR", "Debut": "FFI", "EQUIPO": "DRAGONES-DE-FUEGO" },
    
    { "Nombre": "BUDDY-FURY", "Curso": "3º", "Elemento": "Montaña", "Posición": "MD",
      "Género": "M", "Invocador": "Totem", "Dorsal": "6", "Nacionalidad": "JAP", "Debut": "GCG", "EQUIPO": "EARTH-ELEVEN" },
    
    { "Nombre": "BUNNY-COTTONTAIL", "Curso": "1º", "Elemento": "Aire", "Posición": "DL",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "17", "Nacionalidad": "JAP", "Debut": "FF_ARES", "EQUIPO": "ALPINO_(ARES)" },
    
    { "Nombre": "BYRON-LOVE", "Curso": "2º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "9", "Nacionalidad": "KOR", "Debut": "FF", "EQUIPO": "DRAGONES-DE-FUEGO" },

    ### C ###
    
    { "Nombre": "CALEB-STONEWALL", "Curso": "2º", "Elemento": "Fuego", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "8", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "INAZUMA-JAPON" },
    
    { "Nombre": "CALEB-STONEWALL_(ADULTO)", "Curso": "ADULTO", "Elemento": "Fuego", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "NEO-JAPON_(RESISTENCIA-DE-JAPON)" },
    
    { "Nombre": "CALEB-STONEWALL_(REDUX)", "Curso": "2º", "Elemento": "Fuego", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ROYAL-ACADEMY_REDUX" },
    
    { "Nombre": "CELIA-HILLS", "Curso": "1º", "Elemento": "Aire", "Posición": "MD",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "-", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "EQUIPO-FEMENINO" },
    
    { "Nombre": "CERISE-BLOSSOM", "Curso": "2º", "Elemento": "Aire", "Posición": "MD",
      "Género": "F", "Invocador": "Totem", "Dorsal": "7", "Nacionalidad": "JAP", "Debut": "GCG", "EQUIPO": "EARTH-ELEVEN" },
      
    { "Nombre": "CLAUDE-BEACONS", "Curso": "2º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Nacionalidad": "KOR", "Debut": "FFI", "EQUIPO": "DRAGONES-DE-FUEGO" },
        
    { "Nombre": "CRONUS-FOURSEASONS", "Curso": "2º", "Elemento": "Fuego", "Posición": "MD",
      "Género": "M", "Invocador": "EG", "Dorsal": "9", "EQUIPO": "MONTE-OLIMPO" },
    
    { "Nombre": "CRONUS-FOURSEASONS_(RESISTENCIA)", "Curso": "2º", "Elemento": "Fuego", "Posición": "MD",
      "Género": "M", "Invocador": "EG", "Dorsal": "5", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "NEO-JAPON_(RESISTENCIA-DE-JAPON)" },
    
    ### D ###
    { "Nombre": "DANIEL-HATCH", "Curso": "2º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "9", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ROYAL-ACADEMY" },
    
    { "Nombre": "DARREN-LACHANCE", "Curso": "1º", "Elemento": "Bosque", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "12", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "RAIMON_II" },
      
    { "Nombre": "DAVE-QUAGMIRE", "Curso": "3º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "NEO-JAPON" },

    { "Nombre": "DAVID-SAMFORD", "Curso": "2º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ROYAL-ACADEMY" },
    
    { "Nombre": "DAVID-SAMFORD_(INAZUMA)", "Curso": "2º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "16", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "INAZUMA-JAPON" },
      
    { "Nombre": "DAVID-SAMFORD_(LEGENDARIO)", "Curso": "ADULTO", "Elemento": "Bosque", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "16", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "INAZUMA-JAPON_LEGENDARIO" },
      
    { "Nombre": "DAVID-SAMFORD_(REDUX)", "Curso": "2º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ROYAL-ACADEMY_REDUX" },
      
    { "Nombre": "DAVY-JONES", "Curso": "2º", "Elemento": "Aire", "Posición": "DL",
      "Género": "M", "Invocador": "EG", "Dorsal": "11", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "NEO-JAPON_(RESISTENCIA-DE-JAPON)" },

    { "Nombre": "JONAS-DEMETRIUS_DEMETER", "Curso": "2º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "9", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ZEUS" },

    { "Nombre": "DEREK-SWING", "Curso": "1º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "8", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ROYAL-ACADEMY" },
    
    { "Nombre": "DESTIN-BILLOWS", "Curso": "1º", "Elemento": "Bosque", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Nacionalidad": "JAP", "Debut": "FF_VR", "EQUIPO": "SOUTH-CIRRUS" },

    { "Nombre": "DANNY-WOOD_DIONYSUS", "Curso": "1º", "Elemento": "Bosque", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "5", "Nacionalidad": "JAP", "Debut": "FF_VR", "EQUIPO": "SOUTH-CIRRUS" },
    
    { "Nombre": "DAVE-QUAGMIRE_(DVALIN)", "Curso": "3º", "Elemento": "Fuego", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(EPSILON)" },

    ### E ###

    { "Nombre": "ELLIOT-EMBER_(ORION)", "Curso": "1º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Nacionalidad": "JAP", "Debut": "FF_ARES", "EQUIPO": "INAZUMA-JAPON_(ORION)" },
      
    { "Nombre": "ERIK-EAGLE", "Curso": "2º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "16", "Nacionalidad": "EEUU", "Debut": "FF", "EQUIPO": "RAIMON" },
      
    { "Nombre": "ERIK-EAGLE_(UNICORN)", "Curso": "2º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "7", "Nacionalidad": "EEUU", "Debut": "FF", "EQUIPO": "UNICORN" },
      
    { "Nombre": "EUGENE-PEABODY", "Curso": "2º", "Elemento": "Aire", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "7", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },

    ### F ###
    
    { "Nombre": "FALCO-FLASHMAN", "Curso": "2º", "Elemento": "Aire", "Posición": "DL",
      "Género": "M", "Invocador": "Totem", "Dorsal": "11", "Nacionalidad": "JAP", "Debut": "GCG", "EQUIPO": "EARTH-ELEVEN" },
      
    { "Nombre": "FEI-RUNE", "Curso": "Por_Definir", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "LOS-ARIONS" },
      
    { "Nombre": "FEI-RUNE_(CS)", "Curso": "Por_Definir", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "11", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "CHRONO-STORM" },
      
    { "Nombre": "FLORA", "Curso": "Por_Definir", "Elemento": "Aire", "Posición": "DL",
      "Género": "F", "Invocador": "EG_ARM", "Dorsal": "12", "Nacionalidad": "Por_definir", "Debut": "Por_definir", "EQUIPO": "DESESPERDIDOS" },
      
    { "Nombre": "FRANK-FOREMAN", "Curso": "2º", "Elemento": "Fuego", "Posición": "DF",
      "Género": "M", "Invocador": "Totem", "Dorsal": "5", "Nacionalidad": "JAP", "Debut": "GCG", "EQUIPO": "EARTH-ELEVEN" },
    
    ### G ###

    { "Nombre": "GABRIEL-GARCÍA", "Curso": "2º", "Elemento": "Bosque", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "3", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "GABRIEL-GARCÍA_(CS)", "Curso": "2º", "Elemento": "Bosque", "Posición": "DF",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "3", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "CHRONO-STORM" },
      
    { "Nombre": "GAMMA", "Curso": "Por_Definir", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "10", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_3.0" },
      
    { "Nombre": "BRYCE-WITHINGALE_(GAZELLE)", "Curso": "2º", "Elemento": "Aire", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "9", "Nacionalidad": "KOR", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(CAOS)" },
      
    { "Nombre": "GOLDIE-LEMMON_(CS)", "Curso": "1º", "Elemento": "Fuego", "Posición": "DF",
      "Género": "F", "Invocador": "EG_ARM", "Dorsal": "78", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "CHRONO-STORM" }, 

    { "Nombre": "GUS-MARTIN", "Curso": "2º", "Elemento": "Bosque", "Posición": "DF",
    "Género": "M", "Invocador": "EG-N", "Dorsal": "5", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ROYAL-ACADEMY" },

    { "Nombre": "GUS-MARTIN_(ADULTO)", "Curso": "ADULTO", "Elemento": "Bosque", "Posición": "DF",
    "Género": "M", "Invocador": "EG-N", "Dorsal": "25", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "EQUIPO-ZERO" },

    ### H ###

    { "Nombre": "HARROLD-HOUDINI_(RESISTENCIA)", "Curso": "3º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG", "Dorsal": "3", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "NEO-JAPON_(RESISTENCIA-DE-JAPON)" },
      
    { "Nombre": "HECTOR-HELIO", "Curso": "2º", "Elemento": "Fuego", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Nacionalidad": "COS", "Debut": "FFI", "EQUIPO": "THE-LITTLE-GIANTS" },

    { "Nombre": "HENRY-HOUSE_HERA", "Curso": "3º", "Elemento": "Fuego", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ZEUS" },

    { "Nombre": "ARION-MATLOCK_HERMES", "Curso": "2º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "7", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ZEUS" },

    { "Nombre": "JEFF-IRON_HEPHESTUS", "Curso": "3º", "Elemento": "Fuego", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "3", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ZEUS" },
    
    { "Nombre": "HERMAN-WALDON", "Curso": "2º", "Elemento": "Aire", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "6", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ROYAL-ACADEMY" },
      
    { "Nombre": "HOTEL", "Curso": "Por_Definir", "Elemento": "Montaña", "Posición": "PR",
      "Género": "M", "Invocador": "EG", "Dorsal": "1", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_1.0" },
      
    { "Nombre": "HUGUES-BAUDET", "Curso": "2º", "Elemento": "Aire", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "13", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "XAVIER-FOSTER_(HUNTER)", "Curso": "3º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Nacionalidad": "JAP", "Debut": "FF_ARES", "EQUIPO": "ACADEMIA-ALIA" },

    { "Nombre": "XAVIER-FOSTER_(HUNTER_ORION)", "Curso": "3º", "Elemento": "Fuego", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "15", "Nacionalidad": "JAP", "Debut": "FF_ARES", "EQUIPO": "INAZUMA-JAPON_(ORION)" },
      
    { "Nombre": "HURLEY-KANE", "Curso": "3º", "Elemento": "Aire", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "4", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "RAIMON_II" },
      
    ### I ### 
    ### J ###
    
    { "Nombre": "JACK-WALLSIDE", "Curso": "1º", "Elemento": "Montaña", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "3", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },

    { "Nombre": "JOHN-BLOOM", "Curso": "2º", "Elemento": "Aire", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "7", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ROYAL-ACADEMY" },
    
    { "Nombre": "JORDAN-GREENWAY_(JANUS)", "Curso": "2º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(TORMENTA-DE-GEMINIS)" },
      
    { "Nombre": "JEAN-PIERRE-LAPAN", "Curso": "1º", "Elemento": "Montaña", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "5", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "JEAN-PIERRE-LAPAN_(CS)", "Curso": "1º", "Elemento": "Montaña", "Posición": "PR",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "20", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "CHRONO-STORM" },

    { "Nombre": "JIM-WRAITH", "Curso": "2º", "Elemento": "Bosque", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "4",  "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },

    { "Nombre": "JUDE-SHARP_(ROYAL)", "Curso": "2º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10",  "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ROYAL-ACADEMY" },
    
    { "Nombre": "JUDE-SHARP", "Curso": "2º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "14",   "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },

    { "Nombre": "JOSEPH-KING", "Curso": "2º", "Elemento": "Fuego", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1",   "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ROYAL-ACADEMY" },
      
    { "Nombre": "JOSEPH-KING_(NEO)", "Curso": "2º", "Elemento": "Fuego", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1",   "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "NEO-JAPON" },
      
    { "Nombre": "JOSEPH-KING_(REDUX)", "Curso": "2º", "Elemento": "Fuego", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1",   "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ROYAL-ACADEMY_REDUX" },
      
    { "Nombre": "JORDAN-GREENWAY", "Curso": "2º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "13",   "Nacionalidad": "JAP", "Debut": "FFI", "EQUIPO": "INAZUMA-JAPON" },
      
    { "Nombre": "JULIETA", "Curso": "Por_Definir", "Elemento": "Bosque", "Posición": "DL",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "9",   "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_1.0" },
      
    ### K ###

    { "Nombre": "KEENAN-SHARPE", "Curso": "1º", "Elemento": "Montaña", "Posición": "DF",
      "Género": "M", "Invocador": "Totem", "Dorsal": "3",   "Nacionalidad": "JAP", "Debut": "GCG", "EQUIPO": "EARTH-ELEVEN" },
      
    { "Nombre": "KEVIN-DRAGONFLY", "Curso": "2º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11",   "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },
      
    { "Nombre": "KEVIN-DRAGONFLY_(ARES)", "Curso": "3º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "19",   "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ALPINO_(ARES)" },  

    ### L ###

    { "Nombre": "LUCIAN-DARK", "Curso": "1º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "16",   "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
       
    ### M ###
    
    { "Nombre": "MARK-EVANS", "Curso": "2º", "Elemento": "Montaña", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },
      
    { "Nombre": "MARK-EVANS_(II)", "Curso": "2º", "Elemento": "Montaña", "Posición": "DF_LB",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "15", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON_II" },
      
    { "Nombre": "MARK-EVANS_(ADULTO)", "Curso": "ADULTO", "Elemento": "Montaña", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "MARK-EVANS_(ARIONS)", "Curso": "2º", "Elemento": "Montaña", "Posición": "PR",
      "Género": "M", "Invocador": "EG", "Dorsal": "1", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "LOS-ARIONS" },
      
    { "Nombre": "MARK-EVANS_(LEGENDARIO)", "Curso": "ADULTO", "Elemento": "Montaña", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "INAZUMA-JAPON_LEGENDARIO" },
      
    { "Nombre": "MAXWELL-CARSON", "Curso": "2º", "Elemento": "Aire", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "9", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },
      
    { "Nombre": "MARK-EVANS_(MECHAMARK)", "Curso": "Por_Definir", "Elemento": "Montaña", "Posición": "PR",
      "Género": "M", "Invocador": "EG", "Dorsal": "1", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_(EL-DORADO-02)" },
      
    { "Nombre": "MICHAEL-BALLZACK", "Curso": "2º", "Elemento": "Montaña", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "MIKE", "Curso": "Por_Definir", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_1.0" },
      
    { "Nombre": "RAY-DARK_(MISTER-D)", "Curso": "ADULTO", "Elemento": "Montaña", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ORFEO" },   

    ### N ###
    
    { "Nombre": "NATHAN-SWIFT", "Curso": "2º", "Elemento": "Aire", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "2", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },
      
    { "Nombre": "NELLY-RAIMON", "Curso": "2º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "-", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "EQUIPO-FEMENINO" },
      
    { "Nombre": "NIGEL-AUGUST_(NEPPTEN)", "Curso": "2º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(CAOS)" },
      
    { "Nombre": "NJORD-SNIO", "Curso": "2º", "Elemento": "Aire", "Posición": "DL",
      "Género": "M", "Invocador": "EG", "Dorsal": "10", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "ALPINO_(GO)" },
      
    { "Nombre": "NJORD-SNIO_(RESISTENCIA)", "Curso": "2º", "Elemento": "Aire", "Posición": "DL",
      "Género": "M", "Invocador": "EG", "Dorsal": "7", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "NEO-JAPON_(RESISTENCIA-DE-JAPON)" },    

    ### O ###
    ### P ###
    
    { "Nombre": "PAOLO-BIANCHI", "Curso": "2º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Nacionalidad": "ITA", "Debut": "FFI", "EQUIPO": "ORFEO" },
      
    { "Nombre": "PERCIVAL-TRAVIS", "Curso": "ADULTO", "Elemento": "Bosque", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Nacionalidad": "JAP", "Debut": "FFI", "EQUIPO": "INAZUMA-JAPON" },
      
    { "Nombre": "PERCY-HURST_(PERSEO)", "Curso": "2º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Nacionalidad": "JAP", "Debut": "FF_ARES", "EQUIPO": "ZEUS_(ARES)" },

    { "Nombre": "PETER-DRENT", "Curso": "2º", "Elemento": "Montaña", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ROYAL-ACADEMY" },

    { "Nombre": "PAUL-SIDDON_POSEIDON", "Curso": "3º", "Elemento": "Montaña", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ZEUS" },
      
    ### Q ###

    { "Nombre": "QUENTIN-CINQUEDEA_(RESISTENCIA)", "Curso": "2º", "Elemento": "Fuego", "Posición": "PR",
      "Género": "M", "Invocador": "EG", "Dorsal": "1", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "NEO-JAPON_(RESISTENCIA-DE-JAPON)" },    
    
    ### R ###
    
    { "Nombre": "RAY-DARK", "Curso": "ADULTO", "Elemento": "Montaña", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ROYAL-ACADEMY_REDUX" },
      
    { "Nombre": "RICCARDO-DI-RIGO", "Curso": "2º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG", "Dorsal": "9", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "RICCARDO-DI-RIGO_(CS)", "Curso": "2º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "9", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "CHRONO-STORM" },
      
    { "Nombre": "RYOMA-NISHIKI", "Curso": "2º", "Elemento": "Montaña", "Posición": "MD",
      "Género": "M", "Invocador": "EG", "Dorsal": "14", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "RYOMA-NISHIKI_(CS)", "Curso": "2º", "Elemento": "Montaña", "Posición": "MD",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "14", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "CHRONO-STORM" }, 

    ### S ###
    
    { "Nombre": "SAM-KINCAID", "Curso": "1º", "Elemento": "Fuego", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "8", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },
      
    { "Nombre": "SAMGUK-HAN", "Curso": "3º", "Elemento": "Fuego", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "SEYMOUR-HILLMAN", "Curso": "ADULTO", "Elemento": "Montaña", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },
      
    { "Nombre": "SCOTT-BANYAN", "Curso": "1º", "Elemento": "Bosque", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "6", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "RAIMON_II" },
      
    { "Nombre": "SHAWN-FROSTE", "Curso": "2º", "Elemento": "Aire", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "9", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "INAZUMA-JAPON" },
      
    { "Nombre": "SHAWN-FROSTE_(ADULTO)", "Curso": "ADULTO", "Elemento": "Aire", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ALPINO_(GO)" },
      
    { "Nombre": "SHAWN-FROSTE_(AIDEN)", "Curso": "2º", "Elemento": "Aire", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "9", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "RAIMON_II" },
      
    { "Nombre": "SHAWN-FROSTE_(DF)", "Curso": "2º", "Elemento": "Aire", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "9", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "RAIMON_II" },
      
    { "Nombre": "SHAWN-FROSTE_(LEGENDARIO)", "Curso": "ADULTO", "Elemento": "Aire", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "9", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "INAZUMA-JAPON_LEGENDARIO" },
      
    { "Nombre": "SHAWN-FROSTE_(ORION)", "Curso": "3º", "Elemento": "Aire", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "4", "Nacionalidad": "JAP", "Debut": "FF_ARES", "EQUIPO": "INAZUMA-JAPON_(ORION)" },
      
    { "Nombre": "SHUNSUKE-AOYAMA", "Curso": "2º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "12", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "SILVIA-WOODS", "Curso": "2º", "Elemento": "Montaña", "Posición": "PR",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "-", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "EQUIPO-FEMENINO" },
      
    { "Nombre": "SOL-DAYSTAR_(CS)", "Curso": "1º", "Elemento": "Fuego", "Posición": "MD",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "18", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "CHRONO-STORM" },
      
    { "Nombre": "SOR_(CS)", "Curso": "Por_Definir", "Elemento": "Aire", "Posición": "DF",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "21", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "CHRONO-STORM" },
      
    { "Nombre": "STEVE-GRIM", "Curso": "2º", "Elemento": "Aire", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "6", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },
      
    { "Nombre": "SUBARU-HONDA", "Curso": "3º", "Elemento": "Fuego", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "2", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "SUZETTE-HARTLAND", "Curso": "2º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "7", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "RAIMON_II" },
      
    ### T ###

    { "Nombre": "TERRY-ARCHIBALD", "Curso": "2º", "Elemento": "Aire", "Posición": "PR",
      "Género": "M", "Invocador": "Totem", "Dorsal": "1", "Nacionalidad": "JAP", "Debut": "GCG", "EQUIPO": "EARTH-ELEVEN" },
      
    { "Nombre": "TEZCAT", "Curso": "1º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG", "Dorsal": "11", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "EQUIPO-ZERO" },

    { "Nombre": "TIM-SAUNDERS", "Curso": "1º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "7", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },
      
    { "Nombre": "TOD-IRONSIDE", "Curso": "1º", "Elemento": "Fuego", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "5", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },
      
    { "Nombre": "CLAUDE-BEACONS_(TORCH)", "Curso": "2º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Nacionalidad": "KOR", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(CAOS)" },
      
    { "Nombre": "VICTORIA-VANGUARD", "Curso": "2º", "Elemento": "Aire", "Posición": "MD",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "8", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "RAIMON_II" },
      
    { "Nombre": "TRINA-VERDURE", "Curso": "1º", "Elemento": "Bosque", "Posición": "DF",
      "Género": "F", "Invocador": "Totem", "Dorsal": "2", "Nacionalidad": "JAP", "Debut": "GCG", "EQUIPO": "EARTH-ELEVEN" },
      
    { "Nombre": "TYLER-MURDOCK", "Curso": "2º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "14", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "NEO-JAPON" },
      
    ### U ###
    ### V ###

    { "Nombre": "VICTOR-BLADE", "Curso": "1º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG", "Dorsal": "10", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "VICTOR-BLADE_(CS)", "Curso": "1º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "10", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "CHRONO-STORM" },
      
    { "Nombre": "VLADIMIR-BLADE", "Curso": "ADULTO", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "10", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "LOS-ARIONS" },
      
    ### W ###

    { "Nombre": "WANLI-CHANGCHENG", "Curso": "3º", "Elemento": "Montaña", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "4", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "WILLIAM-GLASS", "Curso": "2º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "12", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },

    ### X ###
    
    { "Nombre": "XAVIER-FOSTER", "Curso": "2º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "18", "Nacionalidad": "JAP", "Debut": "FFI", "EQUIPO": "INAZUMA-JAPON" },
      
    { "Nombre": "XAVIER-FOSTER_(SCHILLER)", "Curso": "ADULTO", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "18", "Nacionalidad": "JAP", "Debut": "FFI", "EQUIPO": "INAZUMA-JAPON_LEGENDARIO" },
      
    { "Nombre": "XAVIER-SCHILLER", "Curso": "2º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11",  "Nacionalidad": "JAP", "Debut": "FF_ARES", "EQUIPO": "ACADEMIA-ALIA" },
      
    { "Nombre": "XAVIER-FOSTER_(XENE)", "Curso": "2º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(GENESIS)" },
      
    ### Y ###
    ### Z ###

    { "Nombre": "ZACK-AVALON", "Curso": "3º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "Totem", "Dorsal": "18", "Nacionalidad": "JAP", "Debut": "GCG", "EQUIPO": "EARTH-ELEVEN" },
      
    { "Nombre": "ZANARK-AVALONIC_(CS)", "Curso": "Por_Definir", "Elemento": "Montaña", "Posición": "DL",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "99", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "CHRONO-STORM" },
      
    { "Nombre": "ZIPPY-LERNER", "Curso": "1º", "Elemento": "Aire", "Posición": "DF",
      "Género": "M", "Invocador": "Totem", "Dorsal": "4", "Nacionalidad": "JAP", "Debut": "GCG", "EQUIPO": "EARTH-ELEVEN"}     
]

CharacterRef = [
    ### A ###
    'Adé Kébé', 'Aiden Froste', 'Aitor Cazador', 'Alan Master', 'Alan Master (Neo Japón)', 'Aquilina Schiller',
    'Ares', 'Artemis', 'Austin Hobbes', 'Alex Zabel', 'Alfa', 'Aphrodite', 'Apollo', 'Archer Hawkins', 
    'Arion Sherwind', 'Arion Sherwind (Arions)', 'Arion Sherwind (Chrono Stones)', 
    'Astero Black', 'Athena', 'Axel Blaze', 
    ### B ### 
    'Bai Long', 'Bai Long (Chrono Stones)', 'Bai Long (Resistencia)', 'Bellatrix', 'Beta', 
    'Ben Simmons', 'Bobby Shearer', 'Bobby Shearer (II)', 'Bobby Shearer (Unicorn)',
    'Briar Bloomhurst', 'Bryce Whitingale', 'Buddy Fury', 'Bunny Cottontail', 'Byron Love', 
    ### C ###
    'Caleb Stonewall', 'Caleb Stonewall (Adulto)', 'Caleb Stonewall (Redux)', 'Celia Hills', 
    'Cerise Blossom', 'Claude Beacons', 'Cronus Fourseasons', 'Cronus Fourseasons (Resistencia)',
    ### D ###
    'Daniel Hatch', 'Darren Lachance', 'Dave Quagmire', 'David Samford', 'David Samford (Inazuma Japón)', 
    'David Samford (Legendario)', 'David Samford (Redux)', 'Davy Jones', 'Demetrius', 'Derek Swing', 
    'Destin Billows','Dionysus','Dvalin',
    ### E ###
    'Elliot Ember (Orion)', 'Erik Eagle', 'Erik Eagle (Unicorn)', 'Eugene Peabody', 
    ### F ###
    'Falco Flashman', 'Fei Rune', 'Fei Rune (Chrono Stones)', 'Flora', 'Frank Foreman',
    ### G ###
    'Gabriel García', 'Gabriel García (Chrono Stones)', 'Gamma', 'Gazelle', 
    'Goldie Lemmon (Chrono Stones)', 'Gus Martin', 'Gus Martin (Adulto)',
    ### H ###
    'Harrold Houdini (Resistencia)', 'Hector Helio', 'Hera', 'Hermes', 'Hephestus', 'Herman Waldon', 'Hotel', 'Hugh', 
    'Hunter Foster', 'Hunter Foster (Orion)', 'Hurley Kane', 
    ### J ###
    'Jack Wallside', 'John Bloom', 'Janus', 'Jean-Pierre Lapan', 
    'Jean-Pierre Lapan (Chrono Stones)', 'Jim Wraith', 'Jude Sharp (Royal Academy)', 
    'Jude Sharp', 'Joseph King', 'Joseph King (Neo Japón)', 
    'Joseph King (Redux)', 'Jordan Greenway', 'Julieta', 
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
    'Paolo Bianchi', 'Percival Travis', 'Perseo', 'Peter Drent', 'Poseidón',
    ### Q ###
    'Quentin Cinquedea (Resistencia)',
    ### R ###
    'Ray Dark', 'Riccardo Di Rigo', 'Riccardo Di Rigo (Chrono Stones)', 'Ryoma Nishiki', 'Ryoma Nishiki (Chrono Stones)', 
    ### S ###
    'Sam Kincaid', 'Samguk Han', 'Seymour Hillman', 'Scotty', 'Shawn Froste (Unido)', 
    'Shawn Froste (Adulto)', 'Shawn Froste (Aiden)', 
    'Shawn Froste (DF)', 'Shawn Froste (Legendario)', 'Shawn Froste (Orion)', 
    'Shun', 'Silvia Woods', 'Sol Daystar (Chrono Stones)', 
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
