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

    { "Nombre": "ANGELO-GABRINI", "Curso": "1º", "Elemento": "Aire", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "6", "Nacionalidad": "ITA", "Debut": "FFI", "EQUIPO": "ORFEO" },
    
    { "Nombre": "ANTON-GRAZIUSO", "Curso": "3º", "Elemento": "Fuego", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "4", "Nacionalidad": "ITA", "Debut": "FFI", "EQUIPO": "ORFEO" },

    { "Nombre": "AQUILINA-SCHILLER", "Curso": "ADULTO", "Elemento": "Bosque", "Posición": "DT",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "-", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "RAIMON_II" },

    { "Nombre": "LANE-WAR_ARES", "Curso": "1º", "Elemento": "Aire", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "4", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "NEO-JAPON" },

    { "Nombre": "ARGIE-BARGIE", "Curso": "2º", "Elemento": "Bosque", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "4", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ROYAL-ACADEMY_REDUX" },

    { "Nombre": "ARGIE-BARGIE_NEO", "Curso": "2º", "Elemento": "Bosque", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "4", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "NEO-JAPON" },

    { "Nombre": "ARK", "Curso": "2º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "8", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(GENESIS)" },
    
    { "Nombre": "ARTIE-MISHMAN_ARTEMIS", "Curso": "2º", "Elemento": "Aire", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "6", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ZEUS" },

    { "Nombre": "ASTRAM-SCHILLER", "Curso": "ADULTO", "Elemento": "Bosque", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(GENESIS)" },
    
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

    { "Nombre": "AXEL-BLAZE_INAZUMA", "Curso": "2º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10",  "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "INAZUMA-JAPON" },

    ### B ###
    
    { "Nombre": "BAI-LONG", "Curso": "1º", "Elemento": "Aire", "Posición": "DL",
      "Género": "M", "Invocador": "EG", "Dorsal": "10",  "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "EQUIPO-ZERO" },
    
    { "Nombre": "BAI-LONG_(CS)", "Curso": "1º", "Elemento": "Aire", "Posición": "DL",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "19",  "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "CHRONO-STORM" },
    
    { "Nombre": "BAI-LONG_(RESISTENCIA)", "Curso": "1º", "Elemento": "Aire", "Posición": "DL",
      "Género": "M", "Invocador": "EG", "Dorsal": "10",  "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "NEO-JAPON_(RESISTENCIA-DE-JAPON)" },

    { "Nombre": "BALLER", "Curso": "2º", "Elemento": "Bosque", "Posición": "DF",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "2",  "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(CAOS)" },
    
    { "Nombre": "BELLATRIX", "Curso": "2º", "Elemento": "Aire", "Posición": "MD",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "10",  "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(GENESIS)" },
    
    { "Nombre": "BETA", "Curso": "Por_Definir", "Elemento": "Aire", "Posición": "DL",
      "Género": "F", "Invocador": "EG_ARM", "Dorsal": "10",  "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_2.0" },

    { "Nombre": "BEN-SIMMONS", "Curso": "2º", "Elemento": "Bosque", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "3",  "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ROYAL-ACADEMY" },
    
    { "Nombre": "BOBBY-SHEARER", "Curso": "2º", "Elemento": "Bosque", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "13",  "Nacionalidad": "EEUU", "Debut": "FF", "EQUIPO": "RAIMON" },
    
    { "Nombre": "BOBBY-SHEARER_(UNICORN)", "Curso": "2º", "Elemento": "Bosque", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "5", "Nacionalidad": "EEUU", "Debut": "FF", "EQUIPO": "UNICORN" },

    { "Nombre": "BOMBER", "Curso": "2º", "Elemento": "Fuego", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "4",  "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(CAOS)" },
    
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
    { "Nombre": "CADENCE-SOUNDTOWN", "Curso": "2º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "7", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "MARY-TIMES" },
    
    { "Nombre": "CALEB-STONEWALL", "Curso": "2º", "Elemento": "Fuego", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "8", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "INAZUMA-JAPON" },
    
    { "Nombre": "CALEB-STONEWALL_(ADULTO)", "Curso": "ADULTO", "Elemento": "Fuego", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "NEO-JAPON_(RESISTENCIA-DE-JAPON)" },
    
    { "Nombre": "CALEB-STONEWALL_(REDUX)", "Curso": "2º", "Elemento": "Fuego", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ROYAL-ACADEMY_REDUX" },
    
    { "Nombre": "CELIA-HILLS", "Curso": "1º", "Elemento": "Aire", "Posición": "MG",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "-", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },
    
    { "Nombre": "CERISE-BLOSSOM", "Curso": "2º", "Elemento": "Aire", "Posición": "MD",
      "Género": "F", "Invocador": "Totem", "Dorsal": "7", "Nacionalidad": "JAP", "Debut": "GCG", "EQUIPO": "EARTH-ELEVEN" },

    { "Nombre": "CHANGSU-CHOI", "Curso": "3º", "Elemento": "Fuego", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "7", "Nacionalidad": "KOR", "Debut": "FFI", "EQUIPO": "DRAGONES-DE-FUEGO" },
    
    { "Nombre": "CLAUDE-BEACONS", "Curso": "2º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Nacionalidad": "KOR", "Debut": "ALIUS", "EQUIPO": "DRAGONES-DE-FUEGO" },

    { "Nombre": "CLEAR", "Curso": "2º", "Elemento": "Aire", "Posición": "DF",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "5",  "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(CAOS)" },

    { "Nombre": "CLOAK", "Curso": "2º", "Elemento": "Fuego", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "7",  "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "NEO-JAPON" },
    
    { "Nombre": "CRONUS-FOURSEASONS", "Curso": "2º", "Elemento": "Fuego", "Posición": "MD",
      "Género": "M", "Invocador": "EG", "Dorsal": "9", "Nacionalidad": "JAP", "EQUIPO": "MONTE-OLIMPO" },
    
    { "Nombre": "CRONUS-FOURSEASONS_(RESISTENCIA)", "Curso": "2º", "Elemento": "Fuego", "Posición": "MD",
      "Género": "M", "Invocador": "EG", "Dorsal": "5", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "NEO-JAPON_(RESISTENCIA-DE-JAPON)" },
    
    ### D ###
    { "Nombre": "DANIEL-HATCH", "Curso": "2º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "9", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ROYAL-ACADEMY" },

    { "Nombre": "DANIEL-HATCH_NEO", "Curso": "2º", "Elemento": "Bosque", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "5", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "NEO-JAPON" },

    { "Nombre": "DANTE-DIAVOLO", "Curso": "3º", "Elemento": "Fuego", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "9", "Nacionalidad": "ITA", "Debut": "FFI", "EQUIPO": "ORFEO" },
    
    { "Nombre": "DARREN-LACHANCE", "Curso": "1º", "Elemento": "Bosque", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "RAIMON_II" },

    { "Nombre": "DARREN-LACHANCE_INAZUMA-JAPON", "Curso": "1º", "Elemento": "Bosque", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "20", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "INAZUMA-JAPON" },
      
    { "Nombre": "DAVE-QUAGMIRE", "Curso": "3º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "NEO-JAPON" },

    { "Nombre": "DAVID-EVANS", "Curso": "ADULTO", "Elemento": "Montaña", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Nacionalidad": "JAP", "Debut": "FFI", "EQUIPO": "THE-LITTLE-GIANTS" },
    
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

    { "Nombre": "DIAM", "Curso": "2º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(TORMENTA-DE-GEMINIS)" },
    
    { "Nombre": "DANNY-WOOD_DIONYSUS", "Curso": "1º", "Elemento": "Aire", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "5", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ZEUS" },

    { "Nombre": "DROLL", "Curso": "2º", "Elemento": "Aire", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "7", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(CAOS)" },
    
    { "Nombre": "DAVE-QUAGMIRE_(DVALIN)", "Curso": "3º", "Elemento": "Fuego", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(EPSILON)" },

    { "Nombre": "DYLAN-KEATS", "Curso": "2º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Nacionalidad": "EEUU", "Debut": "FFI", "EQUIPO": "UNICORN" },

    ### E ###

    { "Nombre": "EDGAR-PARTINUS", "Curso": "3º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Nacionalidad": "ENG", "Debut": "FFI", "EQUIPO": "KNIGHTS-OF-QUEEN" },
    
    { "Nombre": "ELLIOT-EMBER_(ORION)", "Curso": "1º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Nacionalidad": "JAP", "Debut": "FF_ARES", "EQUIPO": "INAZUMA-JAPON_(ORION)" },
      
    { "Nombre": "ERIK-EAGLE", "Curso": "2º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "16", "Nacionalidad": "EEUU", "Debut": "FF", "EQUIPO": "RAIMON" },
      
    { "Nombre": "ERIK-EAGLE_(UNICORN)", "Curso": "2º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "7", "Nacionalidad": "EEUU", "Debut": "FF", "EQUIPO": "UNICORN" },

    { "Nombre": "ETHAN-WHITERING", "Curso": "2º", "Elemento": "Fuego", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "6", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "NEO-JAPON" },
      
    { "Nombre": "EUGENE-PEABODY", "Curso": "2º", "Elemento": "Aire", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "12", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },

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

    { "Nombre": "GIACOMO-YANI", "Curso": "2º", "Elemento": "Montaña", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "8", "Nacionalidad": "ITA", "Debut": "FFI", "EQUIPO": "ORFEO" },
    
    { "Nombre": "GIGI-BLASI", "Curso": "3º", "Elemento": "Aire", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Nacionalidad": "ITA", "Debut": "FFI", "EQUIPO": "ORFEO" },

    { "Nombre": "GRANT-ICEWATER_GANYMEDE", "Curso": "2º", "Elemento": "Montaña", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "4", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(TORMENTA-DE-GEMINIS)" },
      
    { "Nombre": "BRYCE-WITHINGALE_(GAZELLE)", "Curso": "2º", "Elemento": "Aire", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "9", "Nacionalidad": "KOR", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(CAOS)" },

    { "Nombre": "GELE", "Curso": "2º", "Elemento": "Aire", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "2", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(GENESIS)" },
    
    { "Nombre": "GOCKER", "Curso": "2º", "Elemento": "Montaña", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "3", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(CAOS)" },

    { "Nombre": "GODRIC-WYLES", "Curso": "ADULTO", "Elemento": "Bosque", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(EMPERADORES-OSCUROS)" },

    { "Nombre": "GOLDIE-LEMMON_(CS)", "Curso": "1º", "Elemento": "Fuego", "Posición": "DF",
      "Género": "F", "Invocador": "EG_ARM", "Dorsal": "78", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "CHRONO-STORM" }, 

    { "Nombre": "GORDON-STAR_GALILEO", "Curso": "2º", "Elemento": "Bosque", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(TORMENTA-DE-GEMINIS)" },

    { "Nombre": "GUS-MARTIN", "Curso": "2º", "Elemento": "Bosque", "Posición": "DF",
    "Género": "M", "Invocador": "EG-N", "Dorsal": "5", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ROYAL-ACADEMY" },

    { "Nombre": "GUS-MARTIN_(ADULTO)", "Curso": "ADULTO", "Elemento": "Bosque", "Posición": "DF",
    "Género": "M", "Invocador": "EG-N", "Dorsal": "25", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "EQUIPO-ZERO" },

    { "Nombre": "GRENT", "Curso": "2º", "Elemento": "Fuego", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(CAOS)" },

    ### H ###

    { "Nombre": "HARROLD-HOUDINI_(RESISTENCIA)", "Curso": "3º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG", "Dorsal": "3", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "NEO-JAPON_(RESISTENCIA-DE-JAPON)" },

    { "Nombre": "HAUSER", "Curso": "2º", "Elemento": "Montaña", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "5", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(GENESIS)" },
    
    { "Nombre": "ETHAN-WHITERING_HEAT", "Curso": "2º", "Elemento": "Fuego", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "6", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(CAOS)" },
    
    { "Nombre": "HECTOR-HELIO", "Curso": "2º", "Elemento": "Fuego", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Nacionalidad": "COS", "Debut": "FFI", "EQUIPO": "THE-LITTLE-GIANTS" },
    
    { "Nombre": "HENRY-HOUSE", "Curso": "3º", "Elemento": "Fuego", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "13", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "NEO-JAPON" },
    
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

    { "Nombre": "HURLEY-KANE_INAZUMA", "Curso": "3º", "Elemento": "Aire", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "4", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "INAZUMA-JAPON" },
      
    ### I ### 
    ### J ###
    
    { "Nombre": "JACK-WALLSIDE", "Curso": "1º", "Elemento": "Montaña", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "3", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },

    { "Nombre": "JACK-WALLSIDE_INAZUMA", "Curso": "1º", "Elemento": "Montaña", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "3", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "INAZUMA-JAPON" },
    
    { "Nombre": "JORDAN-GREENWAY_(JANUS)", "Curso": "2º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(TORMENTA-DE-GEMINIS)" },
      
    { "Nombre": "JEAN-PIERRE-LAPAN", "Curso": "1º", "Elemento": "Montaña", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "5", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "JEAN-PIERRE-LAPAN_(CS)", "Curso": "1º", "Elemento": "Montaña", "Posición": "PR",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "20", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "CHRONO-STORM" },

    { "Nombre": "JIM-WRAITH", "Curso": "2º", "Elemento": "Bosque", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "4",  "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },

    { "Nombre": "JIM-WRAITH_EMPERADORES", "Curso": "2º", "Elemento": "Bosque", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "4",  "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ACADEMIA-ALIUS_(EMPERADORES-OSCUROS)" },

    { "Nombre": "JOHN-BLOOM", "Curso": "2º", "Elemento": "Aire", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "7", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ROYAL-ACADEMY" },

    { "Nombre": "JONAS-DEMETRIUS", "Curso": "2º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "15", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "NEO-JAPON" },

    { "Nombre": "JUDE-SHARP_(ROYAL)", "Curso": "2º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10",  "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ROYAL-ACADEMY" },
    
    { "Nombre": "JUDE-SHARP", "Curso": "2º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "14",   "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },
    
    { "Nombre": "JUDE-SHARP_INAZUMA", "Curso": "2º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "14",   "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "INAZUMA-JAPON" },

    { "Nombre": "JOSEPH-KING", "Curso": "2º", "Elemento": "Fuego", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1",   "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ROYAL-ACADEMY" },
      
    { "Nombre": "JOSEPH-KING_(NEO)", "Curso": "2º", "Elemento": "Fuego", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1",   "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "NEO-JAPON" },
      
    { "Nombre": "JOSEPH-KING_(REDUX)", "Curso": "2º", "Elemento": "Fuego", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1",   "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ROYAL-ACADEMY_REDUX" },
      
    { "Nombre": "JORDAN-GREENWAY", "Curso": "2º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "13",   "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "INAZUMA-JAPON" },
      
    { "Nombre": "JULIETA", "Curso": "Por_Definir", "Elemento": "Bosque", "Posición": "DL",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "9",   "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_1.0" },
      
    ### K ###

    { "Nombre": "KEENAN-SHARPE", "Curso": "1º", "Elemento": "Montaña", "Posición": "DF",
      "Género": "M", "Invocador": "Totem", "Dorsal": "3",   "Nacionalidad": "JAP", "Debut": "GCG", "EQUIPO": "EARTH-ELEVEN" },
      
    { "Nombre": "KEVIN-DRAGONFLY", "Curso": "2º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11",   "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },
      
    { "Nombre": "KEVIN-DRAGONFLY_(ARES)", "Curso": "3º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "19",   "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ALPINO_(ARES)" },

    { "Nombre": "KEVIN-DRAGONFLY_EMPERADORES", "Curso": "2º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11",   "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ACADEMIA-ALIUS_(EMPERADORES-OSCUROS)" },

    { "Nombre": "KEVIN-DRAGONFLY_INAZUMA-JAPON", "Curso": "2º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "17",   "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "INAZUMA-JAPON" },

    { "Nombre": "KIBURN", "Curso": "2º", "Elemento": "Fuego", "Posición": "DF",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "3", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(GENESIS)" },

    { "Nombre": "KIWILL", "Curso": "2º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "f", "Invocador": "EG-N", "Dorsal": "7", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(GENESIS)" },

    { "Nombre": "KORMER", "Curso": "2º", "Elemento": "Fuego", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "6", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(GENESIS)" },

    { "Nombre": "KRYPTO", "Curso": "2º", "Elemento": "Aire", "Posición": "MD",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "7",  "Nacionalidad": "Por_Definir", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(EPSILON)" },

    ### L ###

    { "Nombre": "LUCIAN-DARK", "Curso": "1º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "16",   "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
       
    ### M ###
    
    { "Nombre": "MADDIE-MOONLIGHT", "Curso": "NINO", "Elemento": "Bosque", "Posición": "DL",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "11", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "KFC" },
    
    { "Nombre": "MALCOMN-NIGHT", "Curso": "2º", "Elemento": "Fuego", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "2", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "KIRKWOOD" },

    { "Nombre": "MALCOMN-NIGHT_EMPERADORES-OSCUROS", "Curso": "2º", "Elemento": "Fuego", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "2", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ACADEMIA-ALIUS_(EMPERADORES-OSCUROS)" },

    { "Nombre": "MARCO-MASERATI", "Curso": "2º", "Elemento": "Montaña", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "5", "Nacionalidad": "ITA", "Debut": "FFI", "EQUIPO": "ORFEO" },
      
    { "Nombre": "MARK-EVANS", "Curso": "2º", "Elemento": "Montaña", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },
      
    { "Nombre": "MARK-EVANS_(II)", "Curso": "2º", "Elemento": "Montaña", "Posición": "DF_LB",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "15", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON_II" },

    { "Nombre": "MARK-EVANS_INAZUMA-JAPON", "Curso": "2º", "Elemento": "Montaña", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "INAZUMA-JAPON" },
      
    { "Nombre": "MARK-EVANS_(ADULTO)", "Curso": "ADULTO", "Elemento": "Montaña", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "MARK-EVANS_(ARIONS)", "Curso": "2º", "Elemento": "Montaña", "Posición": "PR",
      "Género": "M", "Invocador": "EG", "Dorsal": "1", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "LOS-ARIONS" },
      
    { "Nombre": "MARK-EVANS_(LEGENDARIO)", "Curso": "ADULTO", "Elemento": "Montaña", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "INAZUMA-JAPON_LEGENDARIO" },

    { "Nombre": "MARK-HILLVALLEY", "Curso": "2º", "Elemento": "Montaña", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "16", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "NEO-JAPON" },

    { "Nombre": "MARK-KRUEGER", "Curso": "2º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "9", "Nacionalidad": "EEUU", "Debut": "FFI", "EQUIPO": "UNICORN" },

    { "Nombre": "MURDOCK_MARVIN", "Curso": "3º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "9", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "KIRKWOOD" },
      
    { "Nombre": "MAXWELL-CARSON", "Curso": "2º", "Elemento": "Aire", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "9", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },

    { "Nombre": "MAXWELL-CARSON_EMPERADORES", "Curso": "2º", "Elemento": "Aire", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "9", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ACADEMIA-ALIUS_(EMPERADORES-OSCUROS)" },
      
    { "Nombre": "MARK-EVANS_(MECHAMARK)", "Curso": "Por_Definir", "Elemento": "Montaña", "Posición": "PR",
      "Género": "M", "Invocador": "EG", "Dorsal": "1", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_(EL-DORADO-02)" },

    { "Nombre": "MERCURY", "Curso": "2º", "Elemento": "Aire", "Posición": "DL",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "9",  "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(EPSILON)" },

    { "Nombre": "METRON", "Curso": "2º", "Elemento": "Aire", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10",  "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(EPSILON)" },
      
    { "Nombre": "MICHAEL-BALLZACK", "Curso": "2º", "Elemento": "Montaña", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "MIKE", "Curso": "Por_Definir", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_1.0" },
      
    { "Nombre": "RAY-DARK_(MISTER-D)", "Curso": "ADULTO", "Elemento": "Montaña", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ORFEO" },   

    ### N ###
    
    { "Nombre": "NATHAN-SWIFT", "Curso": "2º", "Elemento": "Aire", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "2", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },

    { "Nombre": "NATHAN-SWIFT_EMPERADORES", "Curso": "2º", "Elemento": "Aire", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ACADEMIA-ALIUS_(EMPERADORES-OSCUROS)" },

    { "Nombre": "NATHAN-SWIFT_INAZUMA-JAPON", "Curso": "2º", "Elemento": "Aire", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "2", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "INAZUMA-JAPON" },
    
    { "Nombre": "NEIL-TURNER", "Curso": "2º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "BRAIN" },

    { "Nombre": "NEIL-TURNER_NEO", "Curso": "2º", "Elemento": "Fuego", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "6", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "NEO-JAPON" },
      
    { "Nombre": "NELLY-RAIMON", "Curso": "2º", "Elemento": "Fuego", "Posición": "MG",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "-", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },

    { "Nombre": "NELLY-RAIMON_(LITTLE-GIANTS)", "Curso": "2º", "Elemento": "Fuego", "Posición": "MG",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "-", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "THE-LITTLE-GIANTS" },

    { "Nombre": "NERO", "Curso": "2º", "Elemento": "Aire", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1",  "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(GENESIS)" },
      
    { "Nombre": "NIGEL-AUGUST_(NEPPTEN)", "Curso": "2º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(CAOS)" },
      
    { "Nombre": "NJORD-SNIO", "Curso": "2º", "Elemento": "Aire", "Posición": "DL",
      "Género": "M", "Invocador": "EG", "Dorsal": "10", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "ALPINO_(GO)" },
      
    { "Nombre": "NJORD-SNIO_(RESISTENCIA)", "Curso": "2º", "Elemento": "Aire", "Posición": "DL",
      "Género": "M", "Invocador": "EG", "Dorsal": "7", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "NEO-JAPON_(RESISTENCIA-DE-JAPON)" },    

    ### O ###

    { "Nombre": "OTTO-NOBILI", "Curso": "2º", "Elemento": "Bosque", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "3", "Nacionalidad": "ITA", "Debut": "FFI", "EQUIPO": "ORFEO" },    

    
    ### P ###
    { "Nombre": "PANDORA", "Curso": "2º", "Elemento": "Aire", "Posición": "MD",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "6", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(TORMENTA-DE-GEMINIS)" },
    
    { "Nombre": "PAOLO-BIANCHI", "Curso": "2º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Nacionalidad": "ITA", "Debut": "FFI", "EQUIPO": "ORFEO" },

    { "Nombre": "PAUL-PEABODY", "Curso": "1º", "Elemento": "Aire", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "8", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },
    
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
    { "Nombre": "RAFFAELE-GENERANI", "Curso": "2º", "Elemento": "Montaña", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Nacionalidad": "ITA", "Debut": "FFI", "EQUIPO": "ORFEO" },
    
    { "Nombre": "RAY-DARK", "Curso": "ADULTO", "Elemento": "Montaña", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ROYAL-ACADEMY" },
      
    { "Nombre": "RICCARDO-DI-RIGO", "Curso": "2º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG", "Dorsal": "9", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "RICCARDO-DI-RIGO_(CS)", "Curso": "2º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "9", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "CHRONO-STORM" },

    { "Nombre": "RHINE", "Curso": "2º", "Elemento": "Aire", "Posición": "MD",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "8", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(CAOS)" },
    
    { "Nombre": "RIHM", "Curso": "2º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "9", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(TORMENTA-DE-GEMINIS)" },
      
    { "Nombre": "RYOMA-NISHIKI", "Curso": "2º", "Elemento": "Montaña", "Posición": "MD",
      "Género": "M", "Invocador": "EG", "Dorsal": "14", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "RYOMA-NISHIKI_(CS)", "Curso": "2º", "Elemento": "Montaña", "Posición": "MD",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "14", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "CHRONO-STORM" }, 

    ### S ###
    
    { "Nombre": "SAM-KINCAID", "Curso": "1º", "Elemento": "Fuego", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "8", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },

    { "Nombre": "SAM-KINCAID_EMPERADORES", "Curso": "1º", "Elemento": "Fuego", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "8", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ACADEMIA-ALIUS_(EMPERADORES-OSCUROS)" },
      
    { "Nombre": "SAMGUK-HAN", "Curso": "3º", "Elemento": "Fuego", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "SEYMOUR-HILLMAN", "Curso": "ADULTO", "Elemento": "Montaña", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },
      
    { "Nombre": "SCOTT-BANYAN", "Curso": "1º", "Elemento": "Bosque", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "6", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "RAIMON_II" },

    { "Nombre": "SCOTT-BANYAN_INAZUMA", "Curso": "1º", "Elemento": "Bosque", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "6", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "INAZUMA-JAPON" },

    { "Nombre": "SHADOW-CIMMERIAN_RAIMON", "Curso": "2º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "21", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "RAIMON" },

    { "Nombre": "SHADOW-CIMMERIAN", "Curso": "2º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "3", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(EMPERADORES-OSCUROS)" },
    
    { "Nombre": "SHAWN-FROSTE", "Curso": "2º", "Elemento": "Aire", "Posición": "DF_LB",
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
      
    { "Nombre": "SILVIA-WOODS", "Curso": "2º", "Elemento": "Montaña", "Posición": "MG",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "-", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },
      
    { "Nombre": "SOL-DAYSTAR_(CS)", "Curso": "1º", "Elemento": "Fuego", "Posición": "MD",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "18", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "CHRONO-STORM" },
      
    { "Nombre": "SOR_(CS)", "Curso": "Por_Definir", "Elemento": "Aire", "Posición": "DF",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "21", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "CHRONO-STORM" },
      
    { "Nombre": "STEVE-GRIM", "Curso": "2º", "Elemento": "Aire", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "6", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },

    { "Nombre": "STEVE-GRIM_EMPERADORES", "Curso": "2º", "Elemento": "Aire", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "6", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ACADEMIA-ALIUS_(EMPERADORES-OSCUROS)" },
      
    { "Nombre": "SUBARU-HONDA", "Curso": "3º", "Elemento": "Fuego", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "2", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },

     { "Nombre": "SUE-SPARROW", "Curso": "2º", "Elemento": "Aire", "Posición": "MD",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "8", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ROYAL-ACADEMY_REDUX" },
      
    { "Nombre": "SUZETTE-HARTLAND", "Curso": "2º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "7", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "RAIMON_II" },
      
    ### T ###
    { "Nombre": "TALISMAN", "Curso": "1º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "NEO-JAPON" },
    
    { "Nombre": "TERRY-ARCHIBALD", "Curso": "2º", "Elemento": "Aire", "Posición": "PR",
      "Género": "M", "Invocador": "Totem", "Dorsal": "1", "Nacionalidad": "JAP", "Debut": "GCG", "EQUIPO": "EARTH-ELEVEN" },
      
    { "Nombre": "TEZCAT", "Curso": "1º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG", "Dorsal": "11", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "EQUIPO-ZERO" },

    { "Nombre": "THIAGO-TORRES", "Curso": "3º", "Elemento": "Montaña", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "2", "Nacionalidad": "ARG", "Debut": "FFI", "EQUIPO": "LOS-EMPERADORES" },
    
    { "Nombre": "THOR-STOUTBERG", "Curso": "2º", "Elemento": "Aire", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "12", "Nacionalidad": "JAP", "Debut": "FFI", "EQUIPO": "INAZUMA-JAPON" },

    { "Nombre": "TIM-SAUNDERS", "Curso": "1º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "7", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },

    { "Nombre": "TIM-SAUNDERS_EMPERADORES", "Curso": "1º", "Elemento": "Bosque", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "7", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ACADEMIA-ALIUS_(EMPERADORES-OSCUROS)" },
      
    { "Nombre": "TOD-IRONSIDE", "Curso": "1º", "Elemento": "Fuego", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "5", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },

    { "Nombre": "TOD-IRONSIDE_EMPERADORES", "Curso": "1º", "Elemento": "Fuego", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "5", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ACADEMIA-ALIUS_(EMPERADORES-OSCUROS)" },

    { "Nombre": "TOD-IRONSIDE_INAZUMA", "Curso": "1º", "Elemento": "Fuego", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "5", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "INAZUMA-JAPON" },

    { "Nombre": "THOMAS-FELDT", "Curso": "3º", "Elemento": "Bosque", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "BRAIN" },

    { "Nombre": "THOMAS-FELDT_EMPERADORES-OSCUROS", "Curso": "3º", "Elemento": "Bosque", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ACADEMIA-ALIUS_(EMPERADORES-OSCUROS)" },

    { "Nombre": "MURDOCK_THOMAS", "Curso": "3º", "Elemento": "Aire", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "KIRKWOOD" },
      
    { "Nombre": "CLAUDE-BEACONS_(TORCH)", "Curso": "2º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Nacionalidad": "KOR", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(CAOS)" },
      
    { "Nombre": "VICTORIA-VANGUARD", "Curso": "2º", "Elemento": "Aire", "Posición": "MD",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "8", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "RAIMON_II" },
      
    { "Nombre": "TRINA-VERDURE", "Curso": "1º", "Elemento": "Bosque", "Posición": "DF",
      "Género": "F", "Invocador": "Totem", "Dorsal": "2", "Nacionalidad": "JAP", "Debut": "GCG", "EQUIPO": "EARTH-ELEVEN" },

    { "Nombre": "MURDOCK_TYLER", "Curso": "3º", "Elemento": "Montaña", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "KIRKWOOD" },

    { "Nombre": "MURDOCK_TYLER_NEO-JAPON", "Curso": "3º", "Elemento": "Montaña", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "14", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "NEO-JAPON" },
      
    ### U ###
    ### V ###

    { "Nombre": "VICTOR-BLADE", "Curso": "1º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG", "Dorsal": "10", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "VICTOR-BLADE_(CS)", "Curso": "1º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "10", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "CHRONO-STORM" },

    { "Nombre": "VICTOR-GARCIA", "Curso": "3º", "Elemento": "Montaña", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "5", "Nacionalidad": "ES", "Debut": "FFI", "EQUIPO": "LOS-ROJOS" },

    { "Nombre": "VENTO-GAILLANO", "Curso": "2º", "Elemento": "Aire", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "2", "Nacionalidad": "ITA", "Debut": "FFI", "EQUIPO": "ORFEO" },
      
    { "Nombre": "VLADIMIR-BLADE", "Curso": "ADULTO", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "10", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "LOS-ARIONS" },
      
    ### W ###

    { "Nombre": "WANLI-CHANGCHENG", "Curso": "3º", "Elemento": "Montaña", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "4", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "WILLIAM-GLASS", "Curso": "2º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "12", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },

    { "Nombre": "WITTZ", "Curso": "2º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "9", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(GENESIS)" },

    { "Nombre": "WITTZ_NEO", "Curso": "2º", "Elemento": "Bosque", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "9", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "NEO-JAPON" },

    ### X ###
    
    { "Nombre": "XAVIER-FOSTER", "Curso": "2º", "Elemento": "Fuego", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "18", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "INAZUMA-JAPON" },
      
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

    { "Nombre": "ZELL", "Curso": "2º", "Elemento": "Aire", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11",  "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(EPSILON)" },

    { "Nombre": "ZELL_NEO", "Curso": "2º", "Elemento": "Aire", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11",  "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "NEO-JAPON" },
      
    { "Nombre": "ZIPPY-LERNER", "Curso": "1º", "Elemento": "Aire", "Posición": "DF",
      "Género": "M", "Invocador": "Totem", "Dorsal": "4", "Nacionalidad": "JAP", "Debut": "GCG", "EQUIPO": "EARTH-ELEVEN"},  

    { "Nombre": "ZOHEN", "Curso": "2º", "Elemento": "Montaña", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "4", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(GENESIS)" },

    { "Nombre": "ZOHEN_NEO", "Curso": "2º", "Elemento": "Montaña", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "3", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "NEO-JAPON" },
]

CharacterRef = [
    ### A ###
    'Adé Kébé', 'Aiden Froste', 'Aitor Cazador', 'Alan Master', 'Alan Master (Neo Japón)', 'Angelo Gabrini', 'Anton Graziuso', 'Aquilina Schiller',
    'Ares', 'Argie Bargie', 'Argie Bargie (Neo Japón)', 'Ark', 'Artemis', 'Astram Schiller', 'Austin Hobbes', 'Alex Zabel', 'Alfa', 'Aphrodite', 'Apollo', 'Archer Hawkins', 
    'Arion Sherwind', 'Arion Sherwind (Arions)', 'Arion Sherwind (Chrono Stones)', 
    'Astero Black', 'Athena', 'Axel Blaze', 'Axel Blaze (Inazuma Japón)',
    ### B ### 
    'Bai Long', 'Bai Long (Chrono Stones)', 'Bai Long (Resistencia)', 'Baller', 'Bellatrix', 'Beta', 
    'Ben Simmons', 'Bobby Shearer', 'Bobby Shearer (Unicorn)', 'Bomber',
    'Briar Bloomhurst', 'Bryce Whitingale', 'Buddy Fury', 'Bunny Cottontail', 'Byron Love', 
    ### C ###
    'Cadence Soundtown', 'Caleb Stonewall', 'Caleb Stonewall (Adulto)', 'Caleb Stonewall (Redux)', 'Celia Hills', 
    'Cerise Blossom', 'Changsu Choi', 'Claude Beacons', 'Clear', 'Cloak', 'Cronus Fourseasons', 'Cronus Fourseasons (Resistencia)',
    ### D ###
    'Daniel Hatch', 'Daniel Hatch (Neo Japón)', 'Dante Diavolo', 'Darren LaChance', 'Darren LaChance (Inazuma Japón)', 'Dave Quagmire', 
    'David Evans', 'David Samford', 'David Samford (Inazuma Japón)', 
    'David Samford (Legendario)', 'David Samford (Redux)', 'Davy Jones', 'Demetrius', 'Derek Swing', 
    'Destin Billows','Diam', 'Dionysus','Droll', 'Dvalin', 'Dylan Keats',
    ### E ###
    'Edgar Partinus', 'Elliot Ember (Orion)', 'Erik Eagle', 'Erik Eagle (Unicorn)', 'Ethan Whitering', 'Eugene Peabody', 
    ### F ###
    'Falco Flashman', 'Fei Rune', 'Fei Rune (Chrono Stones)', 'Flora', 'Frank Foreman',
    ### G ###
    'Gabriel García', 'Gabriel García (Chrono Stones)', 'Gamma', 
    'Giacomo Yani', 'Gigi Blasi', 'Ganymede', 'Gazelle', 'Gele', 'Gocker', 'Godric Wyles', 
    'Goldie Lemmon (Chrono Stones)', 'Galileo', 'Gus Martin', 'Gus Martin (Adulto)', 'Grent',
    ### H ###
    'Harrold Houdini (Resistencia)', 'Hauser', 'Heat', 'Hector Helio', 'Henry House', 'Hera', 'Hermes', 
    'Hephestus', 'Herman Waldon', 'Hotel', 'Hugh', 
    'Hunter Foster', 'Hunter Foster (Orion)', 'Hurley Kane', 'Hurley Kane (Inazuma Japón)',
    ### J ###
    'Jack Wallside', 'Jack Wallside (Inazuma Japón)', 'Janus', 'Jean-Pierre Lapan', 
    'Jean-Pierre Lapan (Chrono Stones)', 'Jim Wraith', 'Jim Wraith (Emperadores)','John Bloom', 'Jonas', 'Jude Sharp (Royal Academy)', 
    'Jude Sharp', 'Jude Sharp (Inazuma Japon)', 'Joseph King', 'Joseph King (Neo Japón)', 
    'Joseph King (Redux)', 'Jordan Greenway', 'Julieta', 
    ### K ###
    'Keenan Sharpe', 'Kevin Dragonfly', 'Kevin Dragonfly (Ares)', 'Kevin Dragonfly (Emperadores)', 
    'Kevin Dragonfly (Inazuma Japón)', 'Kiburn', 'Kiwill', 'Kormer', 'Krypto',
    ### L ###
    'Lucian Dark', 
    ### M ###
    'Maddie Moonlight', 'Malcomn Night','Malcomn Night (Emperadores)', 'Marco Maserati', 'Mark Evans', 'Mark Evans (II)', 
    'Mark Evans (Inazuma Japón)', 'Mark Evans (Adulto)', 'Mark Evans (Arions)', 'Mark Evans (Legendario)', 'Mark Hillvalley', 'Mark Krueger',
    'Marvin Murdock', 'Max', 'Max (Emperadores', 'Mechamark', 'Mercury', 'Metron', 'Michael Ballzack', 'Mike', 'Mister D', 
    ### N ###
    'Nathan Swift', 'Nathan Swift (Emperadores)', 'Nathan Swift (Inazuma Japón)',
    'Neil Turner', 'Neil Turner (Neo Japón)', 'Nelly Raimon', 'Nero', 'Neppten', 'Njord Snio', 'Njord Snio (Resistencia)',
    ### O ###
    'Otto Nobili', 
    ### P ###
    'Pandora', 'Paolo Bianchi', 'Paul Peabody', 'Percival Travis', 'Perseo', 'Peter Drent', 'Poseidón',
    ### Q ###
    'Quentin Cinquedea (Resistencia)',
    ### R ###
    'Raffaele Generani', 'Ray Dark', 'Riccardo Di Rigo', 'Riccardo Di Rigo (Chrono Stones)', 'Rhine',
    'Rihm', 'Ryoma Nishiki', 'Ryoma Nishiki (Chrono Stones)', 
    ### S ###
    'Sam Kincaid', 'Sam Kincaid (Emperadores)', 'Samguk Han', 'Seymour Hillman', 'Scotty', 'Scotty (Inazuma Japón)',
    'Shadow Cimmerian', 'Shadow Cimmerian (Emperadores)', 'Shawn Froste (Unido)', 
    'Shawn Froste (Adulto)', 'Shawn Froste (Aiden)', 
    'Shawn Froste (DF)', 'Shawn Froste (Legendario)', 'Shawn Froste (Orion)', 
    'Shun', 'Silvia Woods', 'Sol Daystar (Chrono Stones)', 
    'Sor (Chrono Stones)', 'Steve Grim', 'Steve Grim (Emperadores)', 'Subaru Honda', 'Sue Sparrow', 'Sue',
    ### T ###
    'Talisman', 'Terry Archibald', 'Tezcat', 'Thiago Torres', 'Thor Stoutberg', 'Timmy', 'Timmy (Emperadores)', 
    'Tod Ironside', 'Tod Ironside (Emperadores)', 'Tod Ironside (Inazuma Japón)',
    'Thomas Feldt', 'Thomas Feldt (Emperadores)', 'Thomas Murdock',
    'Torch', 'Tori', 'Trina Verdure', 'Tyler Murdock', 'Tyler Murdock (Neo Japón)', 
    ### V ###
    'Victor Blade', 'Victor Blade (Chrono Stones)', 'Victor García', 'Vento Gaillano', 'Vladimir Blade', 
    ### W ###
    'Wanli Changcheng', 'William Glass', 'Wittz', 'Wittz (Neo Japón)',
    ### X ###
    'Xavier Foster', 'Xavier Schiller', 'Xavier Schiller (Ares)', 'Xene', 
    ### Y ###
    ### Z ###
    'Zack Avalon', 'Zanark Avalonic (Chrono Stones)', 'Zell', 'Zell (Neo Japón)', 'Zippy Lerner', 'Zohen', 'Zohen (Neo Japón)',
]
