import flet as ft

Characters = [
    ### A ###
    
    { "Nombre": "ADÉ-KÉBÉ", "Curso": "2º", "Elemento": "AIRE", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "6", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
    
    { "Nombre": "AIDEN-FROSTE", "Curso": "2º", "Elemento": "FUEGO", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF_ARES", "EQUIPO": "ALPINO_(ARES)" },

    { "Nombre": "AIMÉ-QUINTET", "Curso": "2º", "Elemento": "AIRE", "Posición": "DF",
      "Género": "M", "Invocador": "EG", "Dorsal": "2", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "NEO-JAPON_(RESISTENCIA-DE-JAPON)" },
  
    { "Nombre": "AITOR-CAZADOR", "Curso": "1º", "Elemento": "BOSQUE", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "15", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },

    { "Nombre": "ALAN-MASTER", "Curso": "1º", "Elemento": "AIRE", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "4", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ROYAL-ACADEMY" },
    
    { "Nombre": "ALAN-MASTER_(NEO)", "Curso": "1º", "Elemento": "AIRE", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "2", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "NEO-JAPON" },

    { "Nombre": "ALESSANDRO-IL-GRANDE", "Curso": "2º", "Elemento": "MONTAÑA", "Posición": "PR",
      "Género": "M", "Invocador": "EG", "Dorsal": "1", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "MAR-DE-LUNA" },

    { "Nombre": "ANGELO-GABRINI", "Curso": "1º", "Elemento": "AIRE", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "6", "Capitán": "C-N", "Nacionalidad": "ITA", "Debut": "FFI", "EQUIPO": "ORFEO" },
    
    { "Nombre": "ANTON-GRAZIUSO", "Curso": "3º", "Elemento": "FUEGO", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "4", "Capitán": "C-N", "Nacionalidad": "ITA", "Debut": "FFI", "EQUIPO": "ORFEO" },

    { "Nombre": "AQUILINA-SCHILLER", "Curso": "ADULTO_SENIOR", "Elemento": "BOSQUE", "Posición": "DT",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "RAIMON_II" },

    { "Nombre": "AR-ECKS", "Curso": "POR-DEF", "Elemento": "MONTAÑA", "Posición": "MD",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "9", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "CASCADA-PERFECTA" },

    { "Nombre": "LANE-WAR_ARES", "Curso": "1º", "Elemento": "AIRE", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "4", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "NEO-JAPON" },

    { "Nombre": "ARGIE-BARGIE", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "4", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ROYAL-ACADEMY_REDUX" },

    { "Nombre": "ARGIE-BARGIE_NEO", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "4", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "NEO-JAPON" },

    { "Nombre": "ARK", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "8", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(GENESIS)" },
    
    { "Nombre": "ARTIE-MISHMAN_ARTEMIS", "Curso": "2º", "Elemento": "AIRE", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "6", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ZEUS" },

    { "Nombre": "ASTAROTH", "Curso": "POR-DEF", "Elemento": "FUEGO", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Capitán": "C-N", "Nacionalidad": "POR-DEF", "Debut": "FFI", "EQUIPO": "ANGEL-OSCURO" },
    
    { "Nombre": "ASTRAM-SCHILLER", "Curso": "ADULTO_SENIOR", "Elemento": "BOSQUE", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(GENESIS)" },
    
    { "Nombre": "AUSTIN-HOBBES", "Curso": "NIÑO", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FFI", "EQUIPO": "INAZUMA-JAPON" },
    
    { "Nombre": "AXEL-BLAZE_(ALEX-ZABEL)", "Curso": "ADULTO", "Elemento": "FUEGO", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "MONTE-OLIMPO" },
    
    { "Nombre": "ALFA", "Curso": "POR-DEF", "Elemento": "FUEGO", "Posición": "DL",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "10", "Capitán": "C",  "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_1.0" },
    
    { "Nombre": "BYRON-LOVE_(APHRODITE)", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Capitán": "C", "Nacionalidad": "KOR", "Debut": "FF", "EQUIPO": "ZEUS" },

    { "Nombre": "APOLLO-LIGHT_APOLLO", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "2", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ZEUS" },
    
    { "Nombre": "ARCHER-HAWKINS", "Curso": "2º", "Elemento": "AIRE", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "7", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FFI", "EQUIPO": "INAZUMA-JAPON" },
    
    { "Nombre": "ARION-SHERWIND", "Curso": "1º", "Elemento": "AIRE", "Posición": "MD",
      "Género": "M", "Invocador": "EG", "Dorsal": "8", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
    
    { "Nombre": "ARION-SHERWIND_(ARIONS)", "Curso": "1º", "Elemento": "AIRE", "Posición": "DL",
      "Género": "M", "Invocador": "EG", "Dorsal": "8", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "LOS-ARIONS" },
    
    { "Nombre": "ARION-SHERWIND_(CS)", "Curso": "1º", "Elemento": "AIRE", "Posición": "MD",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "8", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "CHRONO-STORM" },

    { "Nombre": "ARION-SHERWIND_(EA)", "Curso": "1º", "Elemento": "AIRE", "Posición": "MD",
      "Género": "M", "Invocador": "TOTEM", "Dorsal": "8", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "EARTH-ELEVEN" },
  
    { "Nombre": "RAY-DARK_(ASTERO-BLACK)", "Curso": "ADULTO_SENIOR", "Elemento": "MONTAÑA", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "GCG", "EQUIPO": "EARTH-ELEVEN" },

    { "Nombre": "RAY-DARK_ASTERO-BLACK_FALAM-MEDIUS", "Curso": "ADULTO_SENIOR", "Elemento": "MONTAÑA", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "96", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "GCG", "EQUIPO": "FALAM-MEDIUS" },
  
    { "Nombre": "WESLEY-KNOX_ATHENA", "Curso": "1º", "Elemento": "BOSQUE", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "8", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ZEUS" },
    
    { "Nombre": "AXEL-BLAZE", "Curso": "2º", "Elemento": "FUEGO", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },

    { "Nombre": "AXEL-BLAZE_INAZUMA", "Curso": "2º", "Elemento": "FUEGO", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "INAZUMA-JAPON" },

    ### B ###
    
    { "Nombre": "BAI-LONG", "Curso": "1º", "Elemento": "AIRE", "Posición": "DL",
      "Género": "M", "Invocador": "EG", "Dorsal": "10", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "EQUIPO-ZERO" },
    
    { "Nombre": "BAI-LONG_(CS)", "Curso": "1º", "Elemento": "AIRE", "Posición": "DL",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "19", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "CHRONO-STORM" },
    
    { "Nombre": "BAI-LONG_(RESISTENCIA)", "Curso": "1º", "Elemento": "AIRE", "Posición": "DL",
      "Género": "M", "Invocador": "EG", "Dorsal": "10", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "NEO-JAPON_(RESISTENCIA-DE-JAPON)" },

    { "Nombre": "BALA-GASGULA", "Curso": "POR-DEF", "Elemento": "FUEGO", "Posición": "DL",
      "Género": "M", "Invocador": "TOTEM", "Dorsal": "11", "Capitán": "C-N", "Nacionalidad": "ALIEN", "Debut": "GCG", "EQUIPO": "FALAM-MEDIUS" },
  
    { "Nombre": "BALLER", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "DF",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "2", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(CAOS)" },

    { "Nombre": "BAY-LAUREL", "Curso": "2º", "Elemento": "MONTAÑA", "Posición": "MD",
      "Género": "M", "Invocador": "EG", "Dorsal": "9", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "KIRKWOOD_GO" },

    { "Nombre": "BAY-LAUREL_(RESISTENCIA)", "Curso": "2º", "Elemento": "MONTAÑA", "Posición": "MD",
      "Género": "M", "Invocador": "EG", "Dorsal": "6", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "NEO-JAPON_(RESISTENCIA-DE-JAPON)" },
    
    { "Nombre": "BELLATRIX", "Curso": "2º", "Elemento": "AIRE", "Posición": "MD",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "10", "Capitán": "C_TEMP", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(GENESIS)" },

    { "Nombre": "BESTIA-NEGRA", "Curso": "POR-DEF", "Elemento": "AIRE", "Posición": "DT",
      "Género": "F", "Invocador": "EG_ARM", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "CIERVO-BLANCO" },
  
    { "Nombre": "BETA", "Curso": "POR-DEF", "Elemento": "AIRE", "Posición": "DL",
      "Género": "F", "Invocador": "EG_ARM", "Dorsal": "10", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_2.0" },

    { "Nombre": "BEN-SIMMONS", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "3", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ROYAL-ACADEMY" },
    
    { "Nombre": "BOBBY-SHEARER", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "13", "Capitán": "C-N", "Nacionalidad": "EEUU", "Debut": "FF", "EQUIPO": "RAIMON" },
    
    { "Nombre": "BOBBY-SHEARER_(UNICORN)", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "5", "Capitán": "C-N", "Nacionalidad": "EEUU", "Debut": "FF", "EQUIPO": "UNICORN" },

    { "Nombre": "BOMBER", "Curso": "2º", "Elemento": "FUEGO", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "4", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(CAOS)" },

    { "Nombre": "BRADFORD-ASH", "Curso": "1º", "Elemento": "MONTAÑA", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "13", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "KIRKWOOD_GO" },

    { "Nombre": "BRAVO", "Curso": "POR-DEF", "Elemento": "MONTAÑA", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "7", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_1.0" },
  
    { "Nombre": "BRIAR-BLOOMHURST", "Curso": "2º", "Elemento": "MONTAÑA", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF_VR", "EQUIPO": "SOUTH-CIRRUS" },
    
    { "Nombre": "BRYCE-WHITINGALE", "Curso": "2º", "Elemento": "AIRE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Capitán": "C-N", "Nacionalidad": "KOR", "Debut": "FFI", "EQUIPO": "DRAGONES-DE-FUEGO" },
    
    { "Nombre": "BUDDY-FURY", "Curso": "3º", "Elemento": "MONTAÑA", "Posición": "MD",
      "Género": "M", "Invocador": "Totem", "Dorsal": "6", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "GCG", "EQUIPO": "EARTH-ELEVEN" },
    
    { "Nombre": "BUNNY-COTTONTAIL", "Curso": "1º", "Elemento": "AIRE", "Posición": "DL",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "17", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF_ARES", "EQUIPO": "ALPINO_(ARES)" },
    
    { "Nombre": "BYRON-LOVE", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "9", "Capitán": "C-N", "Nacionalidad": "KOR", "Debut": "FF", "EQUIPO": "DRAGONES-DE-FUEGO" },

    ### C ###
    
    { "Nombre": "CADENCE-SOUNDTOWN", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "7", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "MARY-TIMES" },
    
    { "Nombre": "CALEB-STONEWALL", "Curso": "2º", "Elemento": "FUEGO", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "8", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "INAZUMA-JAPON" },
    
    { "Nombre": "CALEB-STONEWALL_(ADULTO)", "Curso": "ADULTO", "Elemento": "FUEGO", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "NEO-JAPON_(RESISTENCIA-DE-JAPON)" },
    
    { "Nombre": "CALEB-STONEWALL_(REDUX)", "Curso": "2º", "Elemento": "FUEGO", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ROYAL-ACADEMY_REDUX" },

    { "Nombre": "CALEB-STONEWALL_(RESISTENCIA)", "Curso": "ADULTO", "Elemento": "FUEGO", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "NEO-JAPON_(RESISTENCIA-DE-JAPON)" },
  
    { "Nombre": "CAMELIA-TRAVIS", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "MG",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FFI", "EQUIPO": "INAZUMA-JAPON" },
    
    { "Nombre": "CELIA-HILLS", "Curso": "1º", "Elemento": "AIRE", "Posición": "MG",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },

    { "Nombre": "CELIA-HILLS_ADULTA", "Curso": "ADULTO", "Elemento": "AIRE", "Posición": "MG",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON_(GO)" },
    
    { "Nombre": "CERISE-BLOSSOM", "Curso": "2º", "Elemento": "AIRE", "Posición": "MD",
      "Género": "F", "Invocador": "Totem", "Dorsal": "7", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "GCG", "EQUIPO": "EARTH-ELEVEN" },

    { "Nombre": "CHANGSU-CHOI", "Curso": "3º", "Elemento": "FUEGO", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "7", "Capitán": "C", "Nacionalidad": "KOR", "Debut": "FFI", "EQUIPO": "DRAGONES-DE-FUEGO" },

    { "Nombre": "CHARLIE", "Curso": "POR-DEF", "Elemento": "FUEGO", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "5", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_1.0" },
  
    { "Nombre": "CLARK-WONDERBOT", "Curso": "POR-DEF", "Elemento": "AIRE", "Posición": "DT",
      "Género": "POR-DEF", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "LOS-ARIONS" },
  
    { "Nombre": "CLAUDE-BEACONS", "Curso": "2º", "Elemento": "FUEGO", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Capitán": "C-N", "Nacionalidad": "KOR", "Debut": "ALIUS", "EQUIPO": "DRAGONES-DE-FUEGO" },

    { "Nombre": "CLEAR", "Curso": "2º", "Elemento": "AIRE", "Posición": "DF",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "5", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(CAOS)" },

    { "Nombre": "CLOAK", "Curso": "2º", "Elemento": "FUEGO", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "7",  "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "NEO-JAPON" },
    
    { "Nombre": "CRONUS-FOURSEASONS", "Curso": "2º", "Elemento": "FUEGO", "Posición": "MD",
      "Género": "M", "Invocador": "EG", "Dorsal": "9", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "MONTE-OLIMPO" },
    
    { "Nombre": "CRONUS-FOURSEASONS_(RESISTENCIA)", "Curso": "2º", "Elemento": "FUEGO", "Posición": "MD",
      "Género": "M", "Invocador": "EG", "Dorsal": "5", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "NEO-JAPON_(RESISTENCIA-DE-JAPON)" },
    
    ### D ###
    
    { "Nombre": "DANIEL-HATCH", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "9", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ROYAL-ACADEMY" },

    { "Nombre": "DANIEL-HATCH_NEO", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "5", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "NEO-JAPON" },

    { "Nombre": "DANIELE-SANTINI", "Curso": "2º", "Elemento": "FUEGO", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "12", "Capitán": "C-N", "Nacionalidad": "ITA", "Debut": "FFI", "EQUIPO": "ORFEO" },

    { "Nombre": "DANTE-DIAVOLO", "Curso": "3º", "Elemento": "FUEGO", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "9", "Capitán": "C-N","Nacionalidad": "ITA", "Debut": "FFI", "EQUIPO": "ORFEO" },
    
    { "Nombre": "DARREN-LACHANCE", "Curso": "1º", "Elemento": "BOSQUE", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "RAIMON_II" },

    { "Nombre": "DARREN-LACHANCE_INAZUMA-JAPON", "Curso": "1º", "Elemento": "BOSQUE", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "20", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "INAZUMA-JAPON" },
      
    { "Nombre": "DAVE-QUAGMIRE", "Curso": "3º", "Elemento": "FUEGO", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Capitán": "C","Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "NEO-JAPON" },

    { "Nombre": "DAVE-QUAGMIRE_ADULTO", "Curso": "ADULTO", "Elemento": "FUEGO", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "MONTE-OLIMPO" },

    { "Nombre": "DAVID-EVANS", "Curso": "ADULTO_SENIOR", "Elemento": "MONTAÑA", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FFI", "EQUIPO": "THE-LITTLE-GIANTS" },

    { "Nombre": "DAVID-EVANS_GO", "Curso": "ADULTO_SENIOR", "Elemento": "MONTAÑA", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FFI", "EQUIPO": "RAIMON_CS" },
    
    { "Nombre": "DAVID-SAMFORD", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ROYAL-ACADEMY" },

    { "Nombre": "DAVID-SAMFORD_ADULTO", "Curso": "ADULTO", "Elemento": "BOSQUE", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ROYAL-ACADEMY_GO" },
    
    { "Nombre": "DAVID-SAMFORD_(INAZUMA)", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "16", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "INAZUMA-JAPON" },
      
    { "Nombre": "DAVID-SAMFORD_(LEGENDARIO)", "Curso": "ADULTO", "Elemento": "BOSQUE", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "16", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "INAZUMA-JAPON_LEGENDARIO" },
      
    { "Nombre": "DAVID-SAMFORD_(REDUX)", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ROYAL-ACADEMY_REDUX" },
      
    { "Nombre": "DAVY-JONES", "Curso": "2º", "Elemento": "AIRE", "Posición": "DL",
      "Género": "M", "Invocador": "EG", "Dorsal": "11", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "NEO-JAPON_(RESISTENCIA-DE-JAPON)" },

    { "Nombre": "JONAS-DEMETRIUS_DEMETER", "Curso": "2º", "Elemento": "FUEGO", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "9", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ZEUS" },

    { "Nombre": "DEREK-SWING", "Curso": "1º", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "8", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ROYAL-ACADEMY" },
    
    { "Nombre": "DESTIN-BILLOWS", "Curso": "1º", "Elemento": "BOSQUE", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF_VR", "EQUIPO": "SOUTH-CIRRUS" },

    { "Nombre": "DESTRA", "Curso": "POR-DEF", "Elemento": "MONTAÑA", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Capitán": "C", "Nacionalidad": "POR-DEF", "Debut": "FFI", "EQUIPO": "ANGEL-OSCURO" },
    
    { "Nombre": "DIAM", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(TORMENTA-DE-GEMINIS)" },
    
    { "Nombre": "DANNY-WOOD_DIONYSUS", "Curso": "1º", "Elemento": "AIRE", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "5", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ZEUS" },

    { "Nombre": "DOUG-MCARTHUR", "Curso": "2º", "Elemento": "AIRE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "MAR-DE-LUNA" },

    { "Nombre": "DOUG-MCARTHUR_(RAIMON)", "Curso": "2º", "Elemento": "AIRE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },

    { "Nombre": "DOUG-MCARTHUR_(RESISTENCIA)", "Curso": "2º", "Elemento": "AIRE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "9", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "NEO-JAPON_(RESISTENCIA-DE-JAPON)" },

    { "Nombre": "DRAGO-HILL", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Capitán": "C-N", "Nacionalidad": "COS", "Debut": "FFI", "EQUIPO": "THE-LITTLE-GIANTS" },
    
    { "Nombre": "DROLL", "Curso": "2º", "Elemento": "AIRE", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "7", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(CAOS)" },
    
    { "Nombre": "DAVE-QUAGMIRE_(DVALIN)", "Curso": "3º", "Elemento": "FUEGO", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(EPSILON)" },

    { "Nombre": "DYLAN-KEATS", "Curso": "2º", "Elemento": "FUEGO", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Capitán": "C-N", "Nacionalidad": "EEUU", "Debut": "FFI", "EQUIPO": "UNICORN" },

    ### E ###

    { "Nombre": "ECO", "Curso": "POR-DEF", "Elemento": "BOSQUE", "Posición": "DF",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "3", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_1.0" },
  
    { "Nombre": "EDGAR-PARTINUS", "Curso": "3º", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Capitán": "C", "Nacionalidad": "ENG", "Debut": "FFI", "EQUIPO": "KNIGHTS-OF-QUEEN" },

    { "Nombre": "ELLIOT-EMBER_(ARES)", "Curso": "1º", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF_ARES", "EQUIPO": "POLARIS" },
    
    { "Nombre": "ELLIOT-EMBER_(ORION)", "Curso": "1º", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF_ARES", "EQUIPO": "INAZUMA-JAPON_(ORION)" },
      
    { "Nombre": "ERIK-EAGLE", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "16", "Capitán": "C-N", "Nacionalidad": "EEUU", "Debut": "FF", "EQUIPO": "RAIMON" },
      
    { "Nombre": "ERIK-EAGLE_(UNICORN)", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "7", "Capitán": "C-N", "Nacionalidad": "EEUU", "Debut": "FF", "EQUIPO": "UNICORN" },

    { "Nombre": "ETHAN-WHITERING", "Curso": "2º", "Elemento": "FUEGO", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "6", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "NEO-JAPON" },
      
    { "Nombre": "EUGENE-PEABODY", "Curso": "2º", "Elemento": "AIRE", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "12", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },

    ### F ###
    
    { "Nombre": "FALCO-FLASHMAN", "Curso": "2º", "Elemento": "AIRE", "Posición": "DL",
      "Género": "M", "Invocador": "Totem", "Dorsal": "11", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "GCG", "EQUIPO": "EARTH-ELEVEN" },
      
    { "Nombre": "FEI-RUNE", "Curso": "POR-DEF", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "LOS-ARIONS" },
      
    { "Nombre": "FEI-RUNE_(CS)", "Curso": "POR-DEF", "Elemento": "BOSQUE", "Posición": "MD",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "11", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "CHRONO-STORM" },

    { "Nombre": "FEI-RUNE_GAR", "Curso": "POR-DEF", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "EG", "Dorsal": "9", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "GAR" },
      
    { "Nombre": "FLORA", "Curso": "POR-DEF", "Elemento": "AIRE", "Posición": "DL",
      "Género": "F", "Invocador": "EG_ARM", "Dorsal": "12", "Capitán": "C-N", "Nacionalidad": "POR-DEF", "Debut": "POR-DEF", "EQUIPO": "DESESPERDIDOS" },

    { "Nombre": "FOXTROT", "Curso": "POR-DEF", "Elemento": "AIRE", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "5", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_2.0" },
      
    { "Nombre": "FRANK-FOREMAN", "Curso": "2º", "Elemento": "FUEGO", "Posición": "DF",
      "Género": "M", "Invocador": "Totem", "Dorsal": "5", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "GCG", "EQUIPO": "EARTH-ELEVEN" },
    
    ### G ###

    { "Nombre": "GABRIEL-GARCÍA", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "3", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "GABRIEL-GARCÍA_(CS)", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "DF",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "3", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "CHRONO-STORM" },
      
    { "Nombre": "GAMMA", "Curso": "POR-DEF", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "10", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_3.0" },

    { "Nombre": "GAMMA_ZANARK", "Curso": "POR-DEF", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "10", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_3.0" },

    { "Nombre": "GANDARES-BARAN", "Curso": "POR-DEF", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "TOTEM", "Dorsal": "9", "Capitán": "C-N", "Nacionalidad": "ALIEN", "Debut": "GCG", "EQUIPO": "FALAM-MEDIUS" },
  
    { "Nombre": "GORDON-STAR_GALILEO", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "PR",
    "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(TORMENTA-DE-GEMINIS)" },
  
    { "Nombre": "GARETH-FLARE", "Curso": "2º", "Elemento": "FUEGO", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Capitán": "C-N", "Nacionalidad": "COS", "Debut": "FFI", "EQUIPO": "THE-LITTLE-GIANTS" },

    { "Nombre": "GAIEL", "Curso": "POR-DEF", "Elemento": "AIRE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "8", "Capitán": "C-N", "Nacionalidad": "POR-DEF", "Debut": "FFI", "EQUIPO": "ANGEL-OSCURO" },
    
    { "Nombre": "GIACOMO-YANI", "Curso": "2º", "Elemento": "MONTAÑA", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "8", "Capitán": "C-N", "Nacionalidad": "ITA", "Debut": "FFI", "EQUIPO": "ORFEO" },

    { "Nombre": "GIANLUCA-ZANARDI", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "16", "Capitán": "C-N", "Nacionalidad": "ITA", "Debut": "FFI", "EQUIPO": "ORFEO" },
    
    { "Nombre": "GIGI-BLASI", "Curso": "3º", "Elemento": "AIRE", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Capitán": "C-N", "Nacionalidad": "ITA", "Debut": "FFI", "EQUIPO": "ORFEO" },

    { "Nombre": "GRANT-ICEWATER_GANYMEDE", "Curso": "2º", "Elemento": "MONTAÑA", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "4", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(TORMENTA-DE-GEMINIS)" },
      
    { "Nombre": "BRYCE-WITHINGALE_(GAZELLE)", "Curso": "2º", "Elemento": "AIRE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "9", "Capitán": "C-2", "Nacionalidad": "KOR", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(CAOS)" },

    { "Nombre": "GELE", "Curso": "2º", "Elemento": "AIRE", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "2", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(GENESIS)" },

    { "Nombre": "GHIRIS", "Curso": "POR-DEF", "Elemento": "FUEGO", "Posición": "MD",
      "Género": "M", "Invocador": "EG", "Dorsal": "9", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "RAGNAH" },
    
    { "Nombre": "GOCKER", "Curso": "2º", "Elemento": "MONTAÑA", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "3", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(CAOS)" },

    { "Nombre": "GODRIC-WYLES", "Curso": "ADULTO_SENIOR", "Elemento": "BOSQUE", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(EMPERADORES-OSCUROS)" },

    { "Nombre": "GOLDIE-LEMMON", "Curso": "1º", "Elemento": "FUEGO", "Posición": "LB",
      "Género": "F", "Invocador": "EG", "Dorsal": "78", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "RAIMON_CS" }, 
    
    { "Nombre": "GOLDIE-LEMMON_(CS)", "Curso": "1º", "Elemento": "FUEGO", "Posición": "LB",
      "Género": "F", "Invocador": "EG_ARM", "Dorsal": "78", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "CHRONO-STORM" }, 

    { "Nombre": "GOLF", "Curso": "POR-DEF", "Elemento": "AIRE", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "4", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_1.0" },
  
    { "Nombre": "GOROTA", "Curso": "NIÑO", "Elemento": "FUEGO", "Posición": "DF",
    "Género": "M", "Invocador": "EG-N", "Dorsal": "23", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "RAIMON_CS" }, 
  
    { "Nombre": "GUS-MARTIN", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "DF",
    "Género": "M", "Invocador": "EG-N", "Dorsal": "5", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ROYAL-ACADEMY" },

    { "Nombre": "GUS-MARTIN_(ADULTO)", "Curso": "ADULTO", "Elemento": "BOSQUE", "Posición": "DF",
    "Género": "M", "Invocador": "EG-N", "Dorsal": "25", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "EQUIPO-ZERO" },

    { "Nombre": "GRENT", "Curso": "2º", "Elemento": "FUEGO", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(CAOS)" },

    { "Nombre": "GRISLEY-BEAR", "Curso": "3º", "Elemento": "FUEGO", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "16", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "ALPINO_(GO)" },
    
    ### H ###

    { "Nombre": "HARROLD-HOUDINI_(RESISTENCIA)", "Curso": "3º", "Elemento": "BOSQUE", "Posición": "MD",
      "Género": "M", "Invocador": "EG", "Dorsal": "3", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "NEO-JAPON_(RESISTENCIA-DE-JAPON)" },

    { "Nombre": "HAUSER", "Curso": "2º", "Elemento": "MONTAÑA", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "5", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(GENESIS)" },
    
    { "Nombre": "ETHAN-WHITERING_HEAT", "Curso": "2º", "Elemento": "FUEGO", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "6", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(CAOS)" },

    { "Nombre": "HEBIMOS", "Curso": "POR-DEF", "Elemento": "BOSQUE", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "2", "Capitán": "C-N", "Nacionalidad": "POR-DEF", "Debut": "FFI", "EQUIPO": "ANGEL-OSCURO" },
    
    { "Nombre": "HECTOR-HELIO", "Curso": "2º", "Elemento": "FUEGO", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Capitán": "C", "Nacionalidad": "COS", "Debut": "FFI", "EQUIPO": "THE-LITTLE-GIANTS" },
    
    { "Nombre": "HENRY-HOUSE", "Curso": "3º", "Elemento": "FUEGO", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "13", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "NEO-JAPON" },
    
    { "Nombre": "HENRY-HOUSE_HERA", "Curso": "3º", "Elemento": "FUEGO", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ZEUS" },

    { "Nombre": "ARION-MATLOCK_HERMES", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "7", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ZEUS" },

    { "Nombre": "JEFF-IRON_HEPHESTUS", "Curso": "3º", "Elemento": "FUEGO", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "3", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ZEUS" },
    
    { "Nombre": "HERMAN-WALDON", "Curso": "2º", "Elemento": "AIRE", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "6", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ROYAL-ACADEMY" },

    { "Nombre": "HIDETOSHI-NAKATA", "Curso": "3º", "Elemento": "MONTAÑA", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "7", "Capitán": "C", "Nacionalidad": "ITA", "Debut": "FFI", "EQUIPO": "ORFEO" },
      
    { "Nombre": "HOTEL", "Curso": "POR-DEF", "Elemento": "MONTAÑA", "Posición": "PR",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "1", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_1.0" },
      
    { "Nombre": "HUGUES-BAUDET", "Curso": "2º", "Elemento": "AIRE", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "13", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "XAVIER-FOSTER_(HUNTER)", "Curso": "3º", "Elemento": "FUEGO", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF_ARES", "EQUIPO": "ACADEMIA-ALIA" },

    { "Nombre": "XAVIER-FOSTER_(HUNTER_ORION)", "Curso": "3º", "Elemento": "FUEGO", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "15", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF_ARES", "EQUIPO": "INAZUMA-JAPON_(ORION)" },
      
    { "Nombre": "HURLEY-KANE", "Curso": "3º", "Elemento": "AIRE", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "4", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "RAIMON_II" },

    { "Nombre": "HURLEY-KANE_INAZUMA", "Curso": "3º", "Elemento": "AIRE", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "4", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "INAZUMA-JAPON" },
      
    ### I ### 

    { "Nombre": "IAN-FERRUM", "Curso": "1º", "Elemento": "FUEGO", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "5", "Capitán": "C-N", "Nacionalidad": "COS", "Debut": "FFI", "EQUIPO": "THE-LITTLE-GIANTS" },

    { "Nombre": "ICHIMASA", "Curso": "NIÑO", "Elemento": "AIRE", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "21", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "RAIMON_CS" }, 
  
    { "Nombre": "IGGIE-LOO", "Curso": "1º", "Elemento": "AIRE", "Posición": "DF",
      "Género": "M", "Invocador": "EG", "Dorsal": "5", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "ALPINO_(GO)" },

    { "Nombre": "IGGIE-LOO_(RESISTENCIA)", "Curso": "1º", "Elemento": "AIRE", "Posición": "DF",
      "Género": "M", "Invocador": "EG", "Dorsal": "4", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "NEO-JAPON_(RESISTENCIA-DE-JAPON)" },

    { "Nombre": "INDIA", "Curso": "POR-DEF", "Elemento": "FUEGO", "Posición": "MD",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "8", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_1.0" },
  
    { "Nombre": "INFINITY-BEYOND", "Curso": "2º", "Elemento": "FUEGO", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "PODEROSA-FE" },
    
    ### J ###
    
    { "Nombre": "JACK-WALLSIDE", "Curso": "1º", "Elemento": "MONTAÑA", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "3", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },

    { "Nombre": "JACK-WALLSIDE_INAZUMA", "Curso": "1º", "Elemento": "MONTAÑA", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "3", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "INAZUMA-JAPON" },

    { "Nombre": "JADE-GREENE", "Curso": "2º", "Elemento": "FUEGO", "Posición": "MG",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
    
    { "Nombre": "JORDAN-GREENWAY_(JANUS)", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(TORMENTA-DE-GEMINIS)" },
      
    { "Nombre": "JEAN-PIERRE-LAPIN", "Curso": "1º", "Elemento": "MONTAÑA", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "5", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "JEAN-PIERRE-LAPIN_(CS)", "Curso": "1º", "Elemento": "MONTAÑA", "Posición": "PR",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "20", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "CHRONO-STORM" },

    { "Nombre": "JEAN-PIERRE-LAPIN_(EA)", "Curso": "1º", "Elemento": "MONTAÑA", "Posición": "PR",
      "Género": "M", "Invocador": "TOTEM", "Dorsal": "20", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "EARTH-ELEVEN" },
  
    { "Nombre": "JIM-WRAITH", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "4", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },

    { "Nombre": "JIM-WRAITH_EMPERADORES", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "4",  "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ACADEMIA-ALIUS_(EMPERADORES-OSCUROS)" },

    { "Nombre": "JIMI-GAINES", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "4", "Capitán": "C-N", "Nacionalidad": "COS", "Debut": "FFI", "EQUIPO": "THE-LITTLE-GIANTS" },

    { "Nombre": "JIMMY-KYRK", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "9", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "VIA-LACTEA" },

    { "Nombre": "JIMMY-KYRK_(RESISTENCIA)", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "8", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "NEO-JAPON_(RESISTENCIA-DE-JAPON)" },
  
    { "Nombre": "JINGO", "Curso": "NIÑO", "Elemento": "FUEGO", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "22", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "RAIMON_CS" }, 
  
    { "Nombre": "JOHN-BLOOM", "Curso": "2º", "Elemento": "AIRE", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "7", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ROYAL-ACADEMY" },

    { "Nombre": "JONAS-DEMETRIUS", "Curso": "2º", "Elemento": "FUEGO", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "15", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "NEO-JAPON" },

    { "Nombre": "JORDAN-GREENWAY", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "13", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "INAZUMA-JAPON" },

    { "Nombre": "JOSEPH-KING", "Curso": "2º", "Elemento": "FUEGO", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ROYAL-ACADEMY" },

    { "Nombre": "JOSEPH-KING_(NEO)", "Curso": "2º", "Elemento": "FUEGO", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "NEO-JAPON" },

    { "Nombre": "JOSEPH-KING_(REDUX)", "Curso": "2º", "Elemento": "FUEGO", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ROYAL-ACADEMY_REDUX" },
    
    { "Nombre": "JUDE-SHARP", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "14", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },

    { "Nombre": "JUDE-SHARP_ADULTO", "Curso": "ADULTO", "Elemento": "BOSQUE", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ROYAL-ACADEMY_GO" },
    
    { "Nombre": "JUDE-SHARP_INAZUMA", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "14", "Capitán": "C_TEMP", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "INAZUMA-JAPON" },

    { "Nombre": "JUDE-SHARP_RAIMON-GO", "Curso": "ADULTO", "Elemento": "BOSQUE", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON_(GO)" },

    { "Nombre": "JUDE-SHARP_(ROYAL)", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ROYAL-ACADEMY" },
      
    { "Nombre": "JULIETA", "Curso": "POR-DEF", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "9", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_1.0" },

    { "Nombre": "JULIETA_ZANARK", "Curso": "POR-DEF", "Elemento": "AIRE", "Posición": "DL",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "9", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_3.0" },
  
    ### K ###

    { "Nombre": "KEENAN-DIFORTUNE", "Curso": "1º", "Elemento": "BOSQUE", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "12", "Capitán": "C-N", "Nacionalidad": "COS", "Debut": "FFI", "EQUIPO": "THE-LITTLE-GIANTS" },
    
    { "Nombre": "KEENAN-SHARPE", "Curso": "1º", "Elemento": "MONTAÑA", "Posición": "DF",
      "Género": "M", "Invocador": "Totem", "Dorsal": "3", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "GCG", "EQUIPO": "EARTH-ELEVEN" },

    { "Nombre": "KEITH-RYAN", "Curso": "1º", "Elemento": "FUEGO", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "8", "Capitán": "C-N", "Nacionalidad": "COS", "Debut": "FFI", "EQUIPO": "THE-LITTLE-GIANTS" },
    
    { "Nombre": "KEVIN-DRAGONFLY", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },
      
    { "Nombre": "KEVIN-DRAGONFLY_(ARES)", "Curso": "3º", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "19", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ALPINO_(ARES)" },

    { "Nombre": "KEVIN-DRAGONFLY_EMPERADORES", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ACADEMIA-ALIUS_(EMPERADORES-OSCUROS)" },

    { "Nombre": "KEVIN-DRAGONFLY_INAZUMA-JAPON", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "17", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "INAZUMA-JAPON" },

    { "Nombre": "KIBURN", "Curso": "2º", "Elemento": "FUEGO", "Posición": "DF",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "3", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(GENESIS)" },

    { "Nombre": "KILO", "Curso": "POR-DEF", "Elemento": "BOSQUE", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "3", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_2.0" },

    { "Nombre": "KILO_ZANARK", "Curso": "POR-DEF", "Elemento": "BOSQUE", "Posición": "DF",
       "Género": "M", "Invocador": "EG-N", "Dorsal": "3", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_3.0" },
  
    { "Nombre": "KIWILL", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "MD",
      "Género": "f", "Invocador": "EG-N", "Dorsal": "7", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(GENESIS)" },

    { "Nombre": "KORMER", "Curso": "2º", "Elemento": "FUEGO", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "6", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(GENESIS)" },

    { "Nombre": "KRYPTO", "Curso": "2º", "Elemento": "AIRE", "Posición": "MD",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "7", "Capitán": "C-N", "Nacionalidad": "POR-DEF", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(EPSILON)" },

    ### L ###

    { "Nombre": "LANGFORD-ASH", "Curso": "2º", "Elemento": "MONTAÑA", "Posición": "DL",
      "Género": "M", "Invocador": "EG", "Dorsal": "10", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "KIRKWOOD_GO" },
  
    { "Nombre": "LEPHIEL", "Curso": "POR-DEF", "Elemento": "MONTAÑA", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "5", "Capitán": "C-N", "Nacionalidad": "POR-DEF", "Debut": "FFI", "EQUIPO": "ANGEL-OSCURO" },

    { "Nombre": "LIMA", "Curso": "POR-DEF", "Elemento": "AIRE", "Posición": "MD",
      "Género": "M", "Invocador": "EG", "Dorsal": "6", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_1.0" },

    { "Nombre": "LIMA_ZANARK", "Curso": "POR-DEF", "Elemento": "AIRE", "Posición": "MD",
      "Género": "M", "Invocador": "EG", "Dorsal": "6", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_3.0" },
  
    { "Nombre": "LIU-BEI", "Curso": "ADULTO", "Elemento": "MONTAÑA", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "CHN", "Debut": "CS", "EQUIPO": "RAIMON_CS" }, 
  
    { "Nombre": "LUCIAN-DARK", "Curso": "1º", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "16", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
       
    ### M ###

    { "Nombre": "MAC-ROBINGO", "Curso": "2º", "Elemento": "FUEGO", "Posición": "DL",
    "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Capitán":"C", "Nacionalidad": "BRA", "Debut": "FFI", "EQUIPO": "OS-REIS" },
    
    { "Nombre": "MADDIE-MOONLIGHT", "Curso": "NIÑO", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "11", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "KFC" },
    
    { "Nombre": "MALCOMN-NIGHT", "Curso": "2º", "Elemento": "FUEGO", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "2", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "KIRKWOOD" },

    { "Nombre": "MALCOMN-NIGHT_EMPERADORES-OSCUROS", "Curso": "2º", "Elemento": "FUEGO", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "2", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ACADEMIA-ALIUS_(EMPERADORES-OSCUROS)" },

    { "Nombre": "MALPHAS", "Curso": "POR-DEF", "Elemento": "AIRE", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "6", "Capitán": "C-N", "Nacionalidad": "POR-DEF", "Debut": "FFI", "EQUIPO": "ANGEL-OSCURO" },

    { "Nombre": "MANEUVER-GIBUTSU", "Curso": "POR-DEF", "Elemento": "AIRE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "ALIEN", "Debut": "GCG", "EQUIPO": "FLOTA-IXAR" },
  
    { "Nombre": "MARCO-MASERATI", "Curso": "2º", "Elemento": "MONTAÑA", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "5", "Capitán": "C-N", "Nacionalidad": "ITA", "Debut": "FFI", "EQUIPO": "ORFEO" },
      
    { "Nombre": "MARK-EVANS", "Curso": "2º", "Elemento": "MONTAÑA", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },
      
    { "Nombre": "MARK-EVANS_(II)", "Curso": "2º", "Elemento": "MONTAÑA", "Posición": "DF_LB",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "15", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON_II" },

    { "Nombre": "MARK-EVANS_INAZUMA-JAPON", "Curso": "2º", "Elemento": "MONTAÑA", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "INAZUMA-JAPON" },
      
    { "Nombre": "MARK-EVANS_(ADULTO)", "Curso": "ADULTO", "Elemento": "MONTAÑA", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "MARK-EVANS_(ARIONS)", "Curso": "2º", "Elemento": "MONTAÑA", "Posición": "PR",
      "Género": "M", "Invocador": "EG", "Dorsal": "1", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "LOS-ARIONS" },
      
    { "Nombre": "MARK-EVANS_(LEGENDARIO)", "Curso": "ADULTO", "Elemento": "MONTAÑA", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "INAZUMA-JAPON_LEGENDARIO" },

    { "Nombre": "MARK-HILLVALLEY", "Curso": "2º", "Elemento": "MONTAÑA", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "16", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "NEO-JAPON" },

    { "Nombre": "MARK-KRUEGER", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "9", "Capitán": "C", "Nacionalidad": "EEUU", "Debut": "FFI", "EQUIPO": "UNICORN" },

    { "Nombre": "MURDOCK_MARVIN", "Curso": "3º", "Elemento": "FUEGO", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "9", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "KIRKWOOD" },
      
    { "Nombre": "MAXWELL-CARSON", "Curso": "2º", "Elemento": "AIRE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "9", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },

    { "Nombre": "MAXWELL-CARSON_EMPERADORES", "Curso": "2º", "Elemento": "AIRE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "9", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ACADEMIA-ALIUS_(EMPERADORES-OSCUROS)" },

    { "Nombre": "MAXIM-MILLENNIUM", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "EG", "Dorsal": "10", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "PODEROSA-FE" },
    
    { "Nombre": "MAXIMINO-CRUZ", "Curso": "1º", "Elemento": "AIRE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "9", "Capitán": "C-N", "Nacionalidad": "COS", "Debut": "FFI", "EQUIPO": "THE-LITTLE-GIANTS" },
    
    { "Nombre": "MARK-EVANS_(MECHAMARK)", "Curso": "POR-DEF", "Elemento": "MONTAÑA", "Posición": "PR",
      "Género": "M", "Invocador": "EG", "Dorsal": "1", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_(EL-DORADO-02)" },

    { "Nombre": "MEHR", "Curso": "POR-DEF", "Elemento": "AIRE", "Posición": "MD",
      "Género": "F", "Invocador": "EG", "Dorsal": "8", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "RAGNAH" },

    { "Nombre": "MERCURY", "Curso": "2º", "Elemento": "AIRE", "Posición": "DL",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "9", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(EPSILON)" },

    { "Nombre": "METRON", "Curso": "2º", "Elemento": "AIRE", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(EPSILON)" },
      
    { "Nombre": "MICHAEL-BALLZACK", "Curso": "2º", "Elemento": "MONTAÑA", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "MIKE", "Curso": "POR-DEF", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_1.0" },

    { "Nombre": "MIKE_ZANARK", "Curso": "POR-DEF", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_3.0" },
  
    { "Nombre": "RAY-DARK_(MISTER-D)", "Curso": "ADULTO_SENIOR", "Elemento": "MONTAÑA", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ORFEO" },   

    ### N ###
    
    { "Nombre": "NATHAN-SWIFT", "Curso": "2º", "Elemento": "AIRE", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "2", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },

    { "Nombre": "NATHAN-SWIFT_EMPERADORES", "Curso": "2º", "Elemento": "AIRE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ACADEMIA-ALIUS_(EMPERADORES-OSCUROS)" },

    { "Nombre": "NATHAN-SWIFT_INAZUMA-JAPON", "Curso": "2º", "Elemento": "AIRE", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "2", "Capitán": "C_TEMP", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "INAZUMA-JAPON" },
    
    { "Nombre": "NEIL-TURNER", "Curso": "2º", "Elemento": "FUEGO", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "BRAIN" },

    { "Nombre": "NEIL-TURNER_NEO", "Curso": "2º", "Elemento": "FUEGO", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "6", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "NEO-JAPON" },
      
    { "Nombre": "NELLY-RAIMON", "Curso": "2º", "Elemento": "FUEGO", "Posición": "MG",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },

    { "Nombre": "NELLY-RAIMON_(LITTLE-GIANTS)", "Curso": "2º", "Elemento": "FUEGO", "Posición": "MG",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "THE-LITTLE-GIANTS" },

    { "Nombre": "NENEL", "Curso": "POR-DEF", "Elemento": "FUEGO", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "4", "Capitán": "C-N", "Nacionalidad": "POR-DEF", "Debut": "FFI", "EQUIPO": "ANGEL-OSCURO" },

    { "Nombre": "NERO", "Curso": "2º", "Elemento": "AIRE", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1",  "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(GENESIS)" },
      
    { "Nombre": "NIGEL-AUGUST_(NEPPTEN)", "Curso": "2º", "Elemento": "FUEGO", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(CAOS)" },
      
    { "Nombre": "NJORD-SNIO", "Curso": "2º", "Elemento": "AIRE", "Posición": "DL",
      "Género": "M", "Invocador": "EG", "Dorsal": "10", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "ALPINO_(GO)" },
      
    { "Nombre": "NJORD-SNIO_(RESISTENCIA)", "Curso": "2º", "Elemento": "AIRE", "Posición": "DL",
      "Género": "M", "Invocador": "EG", "Dorsal": "7", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "NEO-JAPON_(RESISTENCIA-DE-JAPON)" },    

    { "Nombre": "NOVIEMBRE", "Curso": "POR-DEF", "Elemento": "FUEGO", "Posición": "MD",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "7", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_2.0" },

    { "Nombre": "NOVIEMBRE_ZANARK", "Curso": "POR-DEF", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_3.0" },

    ### O ###

    { "Nombre": "OGAR-CIRCES", "Curso": "POR-DEF", "Elemento": "MONTAÑA", "Posición": "DF",
      "Género": "M", "Invocador": "TOTEM", "Dorsal": "3", "Capitán": "C-N", "Nacionalidad": "ALIEN", "Debut": "GCG", "EQUIPO": "FALAM-MEDIUS" },
  
    { "Nombre": "OSCAR", "Curso": "POR-DEF", "Elemento": "MONTAÑA", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "2", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_1.0" },

    { "Nombre": "OSCAR_ZANARK", "Curso": "POR-DEF", "Elemento": "MONTAÑA", "Posición": "DF",
       "Género": "M", "Invocador": "EG-N", "Dorsal": "2", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_3.0" },
  
    { "Nombre": "OTTO-NOBILI", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "3", "Capitán": "C-N", "Nacionalidad": "ITA", "Debut": "FFI", "EQUIPO": "ORFEO" },    

    
    ### P ###
    
    { "Nombre": "PADRE-DE-SOR", "Curso": "POR-DEF", "Elemento": "AIRE", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "POR-DEF", "Debut": "CS", "EQUIPO": "RAIMON_CS" },
    
    { "Nombre": "PANDORA", "Curso": "2º", "Elemento": "AIRE", "Posición": "MD",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "6", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(TORMENTA-DE-GEMINIS)" },
    
    { "Nombre": "PAOLO-BIANCHI", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Capitán": "C_TEMP", "Nacionalidad": "ITA", "Debut": "FFI", "EQUIPO": "ORFEO" },

    { "Nombre": "PAPA", "Curso": "POR-DEF", "Elemento": "FUEGO", "Posición": "DF",
       "Género": "M", "Invocador": "EG-N", "Dorsal": "4", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_3.0" },

    { "Nombre": "PAPA_ZANARK", "Curso": "POR-DEF", "Elemento": "FUEGO", "Posición": "DF",
       "Género": "M", "Invocador": "EG-N", "Dorsal": "4", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_3.0" },
  
    { "Nombre": "PAUL-PEABODY", "Curso": "1º", "Elemento": "AIRE", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "8", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },
    
    { "Nombre": "PERCIVAL-TRAVIS", "Curso": "ADULTO_SENIOR", "Elemento": "BOSQUE", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FFI", "EQUIPO": "INAZUMA-JAPON" },

    { "Nombre": "PERCIVAL-TRAVIS_GO", "Curso": "ADULTO", "Elemento": "BOSQUE", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FFI", "EQUIPO": "RAIMON_GO" },
      
    { "Nombre": "PERCY-HURST_(PERSEO)", "Curso": "2º", "Elemento": "FUEGO", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF_ARES", "EQUIPO": "ZEUS_(ARES)" },

    { "Nombre": "PETER-DRENT", "Curso": "2º", "Elemento": "MONTAÑA", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "2", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ROYAL-ACADEMY" },

    { "Nombre": "PHIL-A-MINION", "Curso": "ADULTO", "Elemento": "FUEGO", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "3", "Capitán": "C", "Nacionalidad": "POR-DEF", "Debut": "FFI", "EQUIPO": "ZOOLAN-TEAM" },

    { "Nombre": "PHOBOS", "Curso": "POR-DEF", "Elemento": "MONTAÑA", "Posición": "PR",
      "Género": "M", "Invocador": "TOTEM", "Dorsal": "1", "Capitán": "C-N", "Nacionalidad": "ALIEN", "Debut": "GCG", "EQUIPO": "FLOTA-IXAR" },
  
    { "Nombre": "PAUL-SIDDON_POSEIDON", "Curso": "3º", "Elemento": "MONTAÑA", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ZEUS" },

    { "Nombre": "PRESTON-PRINCETON", "Curso": "1º", "Elemento": "BOSQUE", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "ROYAL-ACADEMY_GO" },

    { "Nombre": "PRINCIPE-CARLOS", "Curso": "ADULTO", "Elemento": "BOSQUE", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "FRA", "Debut": "CS", "EQUIPO": "RAIMON_CS" }, 
  
    ### Q ###

    { "Nombre": "QUEBEC", "Curso": "POR-DEF", "Elemento": "MONTAÑA", "Posición": "MD",
       "Género": "M", "Invocador": "EG-N", "Dorsal": "5", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_3.0" },

    { "Nombre": "QUEBEC_ZANARK", "Curso": "POR-DEF", "Elemento": "MONTAÑA", "Posición": "MD",
       "Género": "M", "Invocador": "EG-N", "Dorsal": "5", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_3.0" },
  
    { "Nombre": "QUENTIN-CINQUEDEA_(RESISTENCIA)", "Curso": "2º", "Elemento": "FUEGO", "Posición": "PR",
      "Género": "M", "Invocador": "EG", "Dorsal": "1", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "NEO-JAPON_(RESISTENCIA-DE-JAPON)" },    

    { "Nombre": "QUINT-HAMPTOM", "Curso": "2º", "Elemento": "AIRE", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "6", "Capitán": "C-N", "Nacionalidad": "COS", "Debut": "FFI", "EQUIPO": "THE-LITTLE-GIANTS" },
    
    ### R ###
    
    { "Nombre": "RAFFAELE-GENERANI", "Curso": "2º", "Elemento": "MONTAÑA", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Capitán": "C-N", "Nacionalidad": "ITA", "Debut": "FFI", "EQUIPO": "ORFEO" },
    
    { "Nombre": "RAY-DARK", "Curso": "ADULTO_SENIOR", "Elemento": "MONTAÑA", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ROYAL-ACADEMY" },

    { "Nombre": "REX-REMINGTON", "Curso": "3º", "Elemento": "MONTAÑA", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "ROYAL-ACADEMY_GO" },

    { "Nombre": "REY-ARTURO", "Curso": "ADULTO", "Elemento": "MONTAÑA", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "CABALLEROS-DE-LA-TABLA-REDONDA" },
  
    { "Nombre": "RICCARDO-DI-RIGO", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "MD",
      "Género": "M", "Invocador": "EG", "Dorsal": "9", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "RICCARDO-DI-RIGO_(CS)", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "MD",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "9", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "CHRONO-STORM" },

    { "Nombre": "RICCARDO-DI-RIGO_(EA)", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "MD",
      "Género": "M", "Invocador": "TOTEM", "Dorsal": "9", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "EARTH-ELEVEN" },
  
    { "Nombre": "RINGO-SATURN", "Curso": "2º", "Elemento": "MONTAÑA", "Posición": "PR",
      "Género": "M", "Invocador": "EG", "Dorsal": "1", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "UNIVERSAL" },

    { "Nombre": "RHINE", "Curso": "2º", "Elemento": "AIRE", "Posición": "MD",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "8", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(CAOS)" },
    
    { "Nombre": "RIHM", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "9", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(TORMENTA-DE-GEMINIS)" },

    { "Nombre": "ROLEIA-ORBES", "Curso": "POR-DEF", "Elemento": "MONTAÑA", "Posición": "MG",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "ALIEN", "Debut": "GCG", "EQUIPO": "FALAM-MEDIUS" },
  
    { "Nombre": "ROMEO", "Curso": "POR-DEF", "Elemento": "AIRE", "Posición": "PR",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "1", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_3.0" },
  
    { "Nombre": "ROMEO_ZANARK", "Curso": "POR-DEF", "Elemento": "AIRE", "Posición": "PR",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "1", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_3.0" },

    { "Nombre": "RONDULA-FLEHL", "Curso": "POR-DEF", "Elemento": "AIRE", "Posición": "MD",
      "Género": "F", "Invocador": "TOTEM", "Dorsal": "6", "Capitán": "C-N", "Nacionalidad": "ALIEN", "Debut": "GCG", "EQUIPO": "FALAM-MEDIUS" },
      
      { "Nombre": "ROSIE-REDD", "Curso": "2º", "Elemento": "AIRE", "Posición": "MG",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
    
    { "Nombre": "RUBU", "Curso": "POR-DEF", "Elemento": "MONTAÑA", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "3", "Capitán": "C-N", "Nacionalidad": "POR-DEF", "Debut": "FFI", "EQUIPO": "ANGEL-OSCURO" },

    { "Nombre": "RUGER-BARAN", "Curso": "POR-DEF", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "TOTEM", "Dorsal": "8", "Capitán": "C-N", "Nacionalidad": "ALIEN", "Debut": "GCG", "EQUIPO": "FALAM-MEDIUS" },
  
    { "Nombre": "RYOMA-NISHIKI", "Curso": "2º", "Elemento": "MONTAÑA", "Posición": "MD",
      "Género": "M", "Invocador": "EG", "Dorsal": "14", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "RYOMA-NISHIKI_(CS)", "Curso": "2º", "Elemento": "MONTAÑA", "Posición": "MD",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "14", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "CHRONO-STORM" }, 

    { "Nombre": "RYOMA-SAKAMOTO", "Curso": "ADULTO", "Elemento": "MONTAÑA", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "29", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "RAIMON_CS" }, 
  
    ### S ###
    
    { "Nombre": "SAM-KINCAID", "Curso": "1º", "Elemento": "FUEGO", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "8", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },

    { "Nombre": "SAM-KINCAID_EMPERADORES", "Curso": "1º", "Elemento": "FUEGO", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "8", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ACADEMIA-ALIUS_(EMPERADORES-OSCUROS)" },
      
    { "Nombre": "SAMGUK-HAN", "Curso": "3º", "Elemento": "FUEGO", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },

    { "Nombre": "SAEL", "Curso": "POR-DEF", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Capitán": "C-2", "Nacionalidad": "POR-DEF", "Debut": "FFI", "EQUIPO": "ANGEL-OSCURO" },
    
    { "Nombre": "SEYMOUR-HILLMAN", "Curso": "ADULTO_SENIOR", "Elemento": "MONTAÑA", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },

    { "Nombre": "SCHEMER-GUILE", "Curso": "ADULTO_SENIOR", "Elemento": "BOSQUE", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "CASCADA-PERFECTA" },
  
    { "Nombre": "SCOTT-BANYAN", "Curso": "1º", "Elemento": "BOSQUE", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "6", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "RAIMON_II" },

    { "Nombre": "SCOTT-BANYAN_INAZUMA", "Curso": "1º", "Elemento": "BOSQUE", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "6", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "INAZUMA-JAPON" },

    { "Nombre": "SHADOW-CIMMERIAN_RAIMON", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "21", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "RAIMON" },

    { "Nombre": "SHADOW-CIMMERIAN", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "3", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(EMPERADORES-OSCUROS)" },
    
    { "Nombre": "SHAWN-FROSTE", "Curso": "2º", "Elemento": "AIRE", "Posición": "DF_LB",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "9", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "INAZUMA-JAPON" },
      
    { "Nombre": "SHAWN-FROSTE_(ADULTO)", "Curso": "ADULTO", "Elemento": "AIRE", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ALPINO_(GO)" },
      
    { "Nombre": "SHAWN-FROSTE_(AIDEN)", "Curso": "2º", "Elemento": "AIRE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "9", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "RAIMON_II" },
      
    { "Nombre": "SHAWN-FROSTE_(DF)", "Curso": "2º", "Elemento": "AIRE", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "9", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "RAIMON_II" },
      
    { "Nombre": "SHAWN-FROSTE_(LEGENDARIO)", "Curso": "ADULTO", "Elemento": "AIRE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "9", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "INAZUMA-JAPON_LEGENDARIO" },
      
    { "Nombre": "SHAWN-FROSTE_(ORION)", "Curso": "3º", "Elemento": "AIRE", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "4", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF_ARES", "EQUIPO": "INAZUMA-JAPON_(ORION)" },

    { "Nombre": "SHISHIMARU", "Curso": "NIÑO", "Elemento": "MONTAÑA", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "24", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "RAIMON_CS" }, 

    { "Nombre": "SHINTARO-NAKAOKA", "Curso": "ADULTO", "Elemento": "BOSQUE", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "RAIMON_CS" }, 
  
    { "Nombre": "SHUNSUKE-AOYAMA", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "12", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },

    { "Nombre": "SIERRA", "Curso": "POR-DEF", "Elemento": "FUEGO", "Posición": "MD",
       "Género": "F", "Invocador": "EG-N", "Dorsal": "7", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_3.0" },
  
    { "Nombre": "SIERRA_ZANARK", "Curso": "POR-DEF", "Elemento": "FUEGO", "Posición": "MD",
       "Género": "F", "Invocador": "EG-N", "Dorsal": "7", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_3.0" },
  
    { "Nombre": "SILVIA-WOODS", "Curso": "2º", "Elemento": "MONTAÑA", "Posición": "MG",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },

    { "Nombre": "SIMEON-AYP", "Curso": "POR-DEF", "Elemento": "MONTAÑA", "Posición": "DL",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "10", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "RAGNAH" },

    { "Nombre": "SKIE_BLUE", "Curso": "1º", "Elemento": "BOSQUE", "Posición": "MG",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },

    { "Nombre": "SOJI-OKITA", "Curso": "ADULTO", "Elemento": "FUEGO", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "17", "Capitán": "C-N", "Nacionalidad": "CHN", "Debut": "CS", "EQUIPO": "ZANARK-DOMAIN" }, 

    { "Nombre": "SOL-DAYSTAR", "Curso": "1º", "Elemento": "FUEGO", "Posición": "DL",
      "Género": "M", "Invocador": "EG", "Dorsal": "11", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "UNIVERSAL" },

    { "Nombre": "SOL-DAYSTAR_(CS)", "Curso": "1º", "Elemento": "FUEGO", "Posición": "MD",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "18", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "CHRONO-STORM" },

    { "Nombre": "SOR", "Curso": "POR-DEF", "Elemento": "AIRE", "Posición": "DF",
      "Género": "M", "Invocador": "EG", "Dorsal": "21", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "RAIMON_CS" },
    
    { "Nombre": "SOR_(CS)", "Curso": "POR-DEF", "Elemento": "AIRE", "Posición": "DF",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "21", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "CHRONO-STORM" },
      
    { "Nombre": "STEVE-GRIM", "Curso": "2º", "Elemento": "AIRE", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "6", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },

    { "Nombre": "STEVE-GRIM_EMPERADORES", "Curso": "2º", "Elemento": "AIRE", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "6", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ACADEMIA-ALIUS_(EMPERADORES-OSCUROS)" },
      
    { "Nombre": "SUBARU-HONDA", "Curso": "3º", "Elemento": "FUEGO", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "2", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },

     { "Nombre": "SUE-SPARROW", "Curso": "2º", "Elemento": "AIRE", "Posición": "MD",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "8", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ROYAL-ACADEMY_REDUX" },
      
    { "Nombre": "SUZETTE-HARTLAND", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "7", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "RAIMON_II" },
      
    ### T ###

    { "Nombre": "TAIAN-INABA", "Curso": "ADULTO", "Elemento": "AIRE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "CIERVO-BLANCO" },
  
    { "Nombre": "TALISMAN", "Curso": "1º", "Elemento": "BOSQUE", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "NEO-JAPON" },

    { "Nombre": "TASUKE", "Curso": "NIÑO", "Elemento": "BOSQUE", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "25", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "RAIMON_CS" }, 
  
    { "Nombre": "TERRY-ARCHIBALD", "Curso": "2º", "Elemento": "AIRE", "Posición": "PR",
      "Género": "M", "Invocador": "Totem", "Dorsal": "1", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "GCG", "EQUIPO": "EARTH-ELEVEN" },
      
    { "Nombre": "TEZCAT", "Curso": "1º", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "EG", "Dorsal": "11", "Capitán": "C-2", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "EQUIPO-ZERO" },

    { "Nombre": "THIAGO-TORRES", "Curso": "3º", "Elemento": "MONTAÑA", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "2", "Capitán": "C", "Nacionalidad": "ARG", "Debut": "FFI", "EQUIPO": "LOS-EMPERADORES" },
    
    { "Nombre": "THOR-STOUTBERG", "Curso": "2º", "Elemento": "AIRE", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "12", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FFI", "EQUIPO": "INAZUMA-JAPON" },

    { "Nombre": "TIM-SAUNDERS", "Curso": "1º", "Elemento": "BOSQUE", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "7", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },

    { "Nombre": "TIM-SAUNDERS_EMPERADORES", "Curso": "1º", "Elemento": "BOSQUE", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "7", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ACADEMIA-ALIUS_(EMPERADORES-OSCUROS)" },
      
    { "Nombre": "TOD-IRONSIDE", "Curso": "1º", "Elemento": "FUEGO", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "5", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },

    { "Nombre": "TOD-IRONSIDE_EMPERADORES", "Curso": "1º", "Elemento": "FUEGO", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "5", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ACADEMIA-ALIUS_(EMPERADORES-OSCUROS)" },

    { "Nombre": "TOD-IRONSIDE_INAZUMA", "Curso": "1º", "Elemento": "FUEGO", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "5", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "INAZUMA-JAPON" },

    { "Nombre": "TOKICHIRO-KINOSHITA", "Curso": "ADULTO", "Elemento": "FUEGO", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "RAIMON_CS" }, 
  
    { "Nombre": "THOMAS-FELDT", "Curso": "3º", "Elemento": "BOSQUE", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "BRAIN" },

    { "Nombre": "THOMAS-FELDT_EMPERADORES-OSCUROS", "Curso": "3º", "Elemento": "BOSQUE", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "ACADEMIA-ALIUS_(EMPERADORES-OSCUROS)" },

    { "Nombre": "MURDOCK_THOMAS", "Curso": "3º", "Elemento": "AIRE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "KIRKWOOD" },
      
    { "Nombre": "CLAUDE-BEACONS_(TORCH)", "Curso": "2º", "Elemento": "FUEGO", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "10", "Capitán": "C", "Nacionalidad": "KOR", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(CAOS)" },
      
    { "Nombre": "VICTORIA-VANGUARD", "Curso": "2º", "Elemento": "AIRE", "Posición": "MD",
      "Género": "F", "Invocador": "EG-N", "Dorsal": "8", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "RAIMON_II" },
      
    { "Nombre": "TRINA-VERDURE", "Curso": "1º", "Elemento": "BOSQUE", "Posición": "DF",
      "Género": "F", "Invocador": "Totem", "Dorsal": "2", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "GCG", "EQUIPO": "EARTH-ELEVEN" },

    { "Nombre": "MURDOCK_TYLER", "Curso": "3º", "Elemento": "MONTAÑA", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "KIRKWOOD" },

    { "Nombre": "MURDOCK_TYLER_NEO-JAPON", "Curso": "3º", "Elemento": "MONTAÑA", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "14", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "NEO-JAPON" },
      
    ### U ###

    
    ### V ###

    { "Nombre": "VICTOR-BLADE", "Curso": "1º", "Elemento": "FUEGO", "Posición": "DL",
      "Género": "M", "Invocador": "EG", "Dorsal": "10", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },
      
    { "Nombre": "VICTOR-BLADE_(CS)", "Curso": "1º", "Elemento": "FUEGO", "Posición": "DL",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "10", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "CHRONO-STORM" },

    { "Nombre": "MANEUVER-GIBUTSU_VICTOR-BLADE", "Curso": "1º", "Elemento": "FUEGO", "Posición": "DL",
      "Género": "M", "Invocador": "EG", "Dorsal": "10", "Capitán": "C-N", "Nacionalidad": "ALIEN", "Debut": "GCG", "EQUIPO": "EARTH-ELEVEN" },

    { "Nombre": "VICTOR-BLADE_FALAM-MEDIUS", "Curso": "1º", "Elemento": "FUEGO", "Posición": "DL",
      "Género": "M", "Invocador": "TOTEM", "Dorsal": "10", "Capitán": "C_TEMP", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "FALAM-MEDIUS" },
  
    { "Nombre": "VICTOR-GARCIA", "Curso": "3º", "Elemento": "MONTAÑA", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "5", "Capitán": "C", "Nacionalidad": "ES", "Debut": "FFI", "EQUIPO": "LOS-ROJOS" },

    { "Nombre": "VENTO-GAILLANO", "Curso": "2º", "Elemento": "AIRE", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "2", "Capitán": "C-N", "Nacionalidad": "ITA", "Debut": "FFI", "EQUIPO": "ORFEO" },
      
    { "Nombre": "VLADIMIR-BLADE", "Curso": "ADULTO", "Elemento": "FUEGO", "Posición": "DL",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "10", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "LOS-ARIONS" },
      
    ### W ###

    { "Nombre": "WANLI-CHANGCHENG", "Curso": "3º", "Elemento": "MONTAÑA", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "4", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "RAIMON_(GO)" },

    { "Nombre": "WALTER-MOUNTAIN", "Curso": "1º", "Elemento": "MONTAÑA", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "3", "Capitán": "C-N", "Nacionalidad": "COS", "Debut": "FFI", "EQUIPO": "THE-LITTLE-GIANTS" },

    { "Nombre": "WENEL", "Curso": "POR-DEF", "Elemento": "FUEGO", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "9", "Capitán": "C-N", "Nacionalidad": "POR-DEF", "Debut": "FFI", "EQUIPO": "ANGEL-OSCURO" },
    
    { "Nombre": "WILLIAM-GLASS", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "12", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "RAIMON" },

    { "Nombre": "WILLIAM-GLASS_INAZUMA-JAPON", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "MG",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF", "EQUIPO": "INAZUMA-JAPON" },

    { "Nombre": "WILLIAM-TODDSFORTH", "Curso": "ADULTO_SENIOR", "Elemento": "FUEGO", "Posición": "DT",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_1.0" },
  
    { "Nombre": "WITTZ", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "9", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(GENESIS)" },

    { "Nombre": "WITTZ_NEO", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "9", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "NEO-JAPON" },

    { "Nombre": "WOLFE-WHYTE", "Curso": "2º", "Elemento": "AIRE", "Posición": "PR",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "1", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "ALPINO_(GO)" },

    ### X ###
    
    { "Nombre": "XAVIER-FOSTER", "Curso": "2º", "Elemento": "FUEGO", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "18", "Capitán": "C_TEMP", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "INAZUMA-JAPON" },
      
    { "Nombre": "XAVIER-FOSTER_(SCHILLER)", "Curso": "ADULTO", "Elemento": "FUEGO", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "18", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FFI", "EQUIPO": "INAZUMA-JAPON_LEGENDARIO" },
      
    { "Nombre": "XAVIER-SCHILLER", "Curso": "2º", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "FF_ARES", "EQUIPO": "ACADEMIA-ALIA" },
      
    { "Nombre": "XAVIER-FOSTER_(XENE)", "Curso": "2º", "Elemento": "FUEGO", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(GENESIS)" },
      
    ### Y ###
    
     { "Nombre": "YASIR-HADDAD", "Curso": "1º", "Elemento": "BOSQUE", "Posición": "MD",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "7", "Capitán": "C-N", "Nacionalidad": "COS", "Debut": "FFI", "EQUIPO": "THE-LITTLE-GIANTS" },
    
    ### Z ###

    { "Nombre": "ZACK-AVALON", "Curso": "3º", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "Totem", "Dorsal": "18", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "GCG", "EQUIPO": "EARTH-ELEVEN" },

    { "Nombre": "ZANARK-AVALONIC", "Curso": "POR-DEF", "Elemento": "MONTAÑA", "Posición": "DT",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "PROTOCOLO-OMEGA_3.0" },

    { "Nombre": "ZANARK-AVALONIC_CAO-CAO", "Curso": "POR-DEF", "Elemento": "MONTAÑA", "Posición": "DF",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "10", "Capitán": "C", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "ZANARK-DOMAIN" },
  
    { "Nombre": "ZANARK-AVALONIC_(CS)", "Curso": "POR-DEF", "Elemento": "MONTAÑA", "Posición": "DL",
      "Género": "M", "Invocador": "EG_ARM", "Dorsal": "99", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CS", "EQUIPO": "CHRONO-STORM" },

    { "Nombre": "ZANOS", "Curso": "POR-DEF", "Elemento": "BOSQUE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "7", "Capitán": "C-N", "Nacionalidad": "POR-DEF", "Debut": "FFI", "EQUIPO": "ANGEL-OSCURO" },

    { "Nombre": "ZAPHOD-RIKER", "Curso": "1º", "Elemento": "AIRE", "Posición": "MD",
      "Género": "M", "Invocador": "EG", "Dorsal": "6", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "CI", "EQUIPO": "VIA-LACTEA" },
    
    { "Nombre": "ZELL", "Curso": "2º", "Elemento": "AIRE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(EPSILON)" },

    { "Nombre": "ZELL_NEO", "Curso": "2º", "Elemento": "AIRE", "Posición": "DL",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "11", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "NEO-JAPON" },
      
    { "Nombre": "ZEPHYR-VITESSE", "Curso": "2º", "Elemento": "AIRE", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "2", "Capitán": "C-N", "Nacionalidad": "COS", "Debut": "FFI", "EQUIPO": "THE-LITTLE-GIANTS" },

    { "Nombre": "ZHUGE-LIANG", "Curso": "ADULTO", "Elemento": "AIRE", "Posición": "MG",
      "Género": "F", "Invocador": "EG", "Dorsal": "-", "Capitán": "C-N", "Nacionalidad": "CHN", "Debut": "CS", "EQUIPO": "RAIMON_CS" }, 
  
    { "Nombre": "ZIPPY-LERNER", "Curso": "1º", "Elemento": "AIRE", "Posición": "DF",
      "Género": "M", "Invocador": "Totem", "Dorsal": "4", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "GCG", "EQUIPO": "EARTH-ELEVEN"},  

    { "Nombre": "ZOHEN", "Curso": "2º", "Elemento": "MONTAÑA", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "4", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "ACADEMIA-ALIUS_(GENESIS)" },

    { "Nombre": "ZOHEN_NEO", "Curso": "2º", "Elemento": "MONTAÑA", "Posición": "DF",
      "Género": "M", "Invocador": "EG-N", "Dorsal": "3", "Capitán": "C-N", "Nacionalidad": "JAP", "Debut": "ALIUS", "EQUIPO": "NEO-JAPON" },
]

CharacterRef = [
    ### A ###
    'Adé Kébé', 'Aiden Froste', 'Aimé Quintet', 'Aitor Cazador', 'Alan Master', 'Alan Master (Neo Japón)', 'Alessandro il Grande', 
    'Angelo Gabrini', 'Anton Graziuso', 'Aquilina Schiller', 'Ar Ecks',
    'Ares', 'Argie Bargie', 'Argie Bargie (Neo Japón)', 'Ark', 'Artemis', 'Astaroth', 
    'Astram Schiller', 'Austin Hobbes', 'Alex Zabel', 'Alfa', 'Aphrodite', 'Apollo', 'Archer Hawkins', 
    'Arion Sherwind', 'Arion Sherwind (Arions)', 'Arion Sherwind (Chrono Storm)', 'Arion Sherwind (Earth Eleven)', 
    'Astero Black', 'Astero Black (Falam Medius)', 'Athena', 'Axel Blaze', 'Axel Blaze (Inazuma Japón)',
    ### B ### 
    'Bai Long', 'Bai Long (Chrono Storm)', 'Bai Long (Resistencia)', 'Bala Gasgula', 'Baller', 'Bay Laurel', 'Bay Laurel (Resistencia)', 'Bellatrix', 
    'Bestia Negra','Beta', 'Ben Simmons', 'Bobby Shearer', 'Bobby Shearer (Unicorn)', 'Bomber', 'Bradford Ash', 'Bravo',
    'Briar Bloomhurst', 'Bryce Whitingale', 'Buddy Fury', 'Bunny Cottontail', 'Byron Love', 
    ### C ###
    'Cadence Soundtown', 'Caleb Stonewall', 'Caleb Stonewall (Adulto)', 'Caleb Stonewall (Redux)', 'Caleb Stonewall (Resistencia)', 
    'Camelia Travis', 'Celia Hills', 'Celia Hills (Adulta)', 
    'Cerise Blossom', 'Changsu Choi', 'Charlie', 'Clark Wonderbot','Claude Beacons', 'Clear', 'Cloak', 'Cronus Fourseasons', 'Cronus Fourseasons (Resistencia)',
    ### D ###
    'Daniel Hatch', 'Daniel Hatch (Neo Japón)', 'Daniele Santini', 'Dante Diavolo', 
    'Darren LaChance', 'Darren LaChance (Inazuma Japón)', 'Dave Quagmire', 'Dave Quagmire (Adulto)', 
    'David Evans', 'David Evans (GO)', 'David Samford', 'David Samford (Adulto)', 'David Samford (Inazuma Japón)', 
    'David Samford (Legendario)', 'David Samford (Redux)', 'Davy Jones', 'Demetrius', 'Derek Swing', 
    'Destin Billows', 'Destra', 'Diam', 'Dionysus', 'Doug McArthur', 'Doug McArthur (Raimon)', 'Doug McArthur (Resistencia)', 'Drago Hill', 'Droll', 'Dvalin', 'Dylan Keats',
    ### E ###
    'Eco', 'Edgar Partinus', 'Elliot Ember (Ares)', 'Elliot Ember (Orion)', 'Erik Eagle', 'Erik Eagle (Unicorn)', 'Ethan Whitering', 'Eugene Peabody', 
    ### F ###
    'Falco Flashman', 'Fei Rune', 'Fei Rune (Chrono Storm)', 'Fei Rune (Gar)', 'Flora', 'Foxtrot', 'Frank Foreman',
    ### G ###
    'Gabriel García', 'Gabriel García (Chrono Storm)', 'Gamma', 'Gamma (MIX Z)', 'Gandares Baran', 'Galileo', 'Gareth Flare', 'Gaiel',
    'Giacomo Yani', 'Gianluca Zanardi', 'Gigi Blasi', 'Ganymede', 'Gazelle', 'Gele', 'Ghiris', 'Gocker', 'Godric Wyles', 
    'Goldie Lemmon', 'Goldie Lemmon (Chrono Storm)', 'Golf', 'Gorota', 'Gus Martin', 'Gus Martin (Adulto)', 'Grent', 'Grisley Bear',
    ### H ###
    'Harrold Houdini (Resistencia)', 'Hauser', 'Heat', 'Hebimos', 'Hector Helio', 'Henry House', 'Hera', 'Hermes', 
    'Hephestus', 'Herman Waldon', 'Hidetoshi Nakata', 'Hotel', 'Hugh', 
    'Hunter Foster', 'Hunter Foster (Orion)', 'Hurley Kane', 'Hurley Kane (Inazuma Japón)',
    ### I ###
    'Ian Ferrum', 'Ichimasa', 'Iggie Loo', 'Iggie Loo (Resistencia)', 'India', 'Infinity Beyond',
    ### J ###
    'Jack Wallside', 'Jack Wallside (Inazuma Japón)', 'Jade Greene', 'Janus', 'Jean-Pierre Lapin', 
    'Jean-Pierre Lapin (Chrono Storm)', 'Jean-Pierre Lapin (Earth Eleven)', 'Jim Wraith', 'Jim Wraith (Emperadores)', 'Jimi Gaines', 'Jimmy Kirk', 'Jimmy Kirk (Resistencia)',
    'Jingo', 'John Bloom', 'Jonas', 'Jordan Greenway', 'Joseph King', 'Joseph King (Neo Japón)', 'Joseph King (Redux)', 'Jude Sharp', 'Jude Sharp (Adulto)',
    'Jude Sharp (Inazuma Japon)', 'Jude Sharp (Raimon GO)', 'Jude Sharp (Royal Academy)', 'Julieta', 'Julieta (MIX Z)',
    ### K ###
    'Keenan DiFortune', 'Keenan Sharpe', 'Keith Ryan', 'Kevin Dragonfly', 'Kevin Dragonfly (Ares)', 'Kevin Dragonfly (Emperadores)', 
    'Kevin Dragonfly (Inazuma Japón)', 'Kiburn', 'Kilo', 'Kilo (MIX Z)', 'Kiwill', 'Kormer', 'Krypto',
    ### L ###
    'Langford Ash', 'Lephiel', 'Lima', 'Lima (MIX Z)', 'Liu Bei', 'Lucian Dark', 
    ### M ###
    'Mac Robingo', 'Maddie Moonlight', 'Malcomn Night','Malcomn Night (Emperadores)', 'Malphas', 'Maneuver Gibutsu','Marco Maserati', 'Mark Evans', 'Mark Evans (II)', 
    'Mark Evans (Inazuma Japón)', 'Mark Evans (Adulto)', 'Mark Evans (Arions)', 'Mark Evans (Legendario)', 'Mark Hillvalley', 'Mark Krueger',
    'Marvin Murdock', 'Max', 'Max (Emperadores)', 'Maxim Millennium', 'Maximino Cruz', 'Mechamark', 'Mehr', 'Mercury', 'Metron', 'Michael Ballzack', 
    'Mike', 'Mike (MIX Z)', 'Mister D', 
    ### N ###
    'Nathan Swift', 'Nathan Swift (Emperadores)', 'Nathan Swift (Inazuma Japón)',
    'Neil Turner', 'Neil Turner (Neo Japón)', 'Nelly Raimon', 'Nelly Raimon (Little Giants)', 'Nenel', 'Nero', 'Neppten', 'Njord Snio', 'Njord Snio (Resistencia)', 
    'Noviembre', 'Noviembre (MIX Z)',
    ### O ###
    'Ogar Circes', 'Oscar', 'Oscar (MIX Z)', 'Otto Nobili', 
    ### P ###
    'Padre de Sor', 'Pandora', 'Paolo Bianchi', 'Papa', 'Papa (MIX Z)', 'Paul Peabody',  'Percival Travis', 'Percival Travis (GO)', 'Perseo', 'Peter Drent', 
    'Phil A. Minion', 'Phobos', 'Poseidón', 'Preston Princeton', 'Príncipe Carlos', 
    ### Q ###
    'Quebec', 'Quebec (MIX Z)','Quentin Cinquedea (Resistencia)', 'Quint Hampton',
    ### R ###
    'Raffaele Generani', 'Ray Dark', 'Rex Remington', 'Rey Arturo', 'Riccardo Di Rigo', 'Riccardo Di Rigo (Chrono Storm)', 'Riccardo Di Rigo (Earth Eleven)', 'Ringo Saturn', 'Rhine',
    'Rihm', 'Roleia Orbes', 'Romeo', 'Romeo (MIX Z)', 'Rondula Flehl', 'Rosie Redd', 'Rubú', 'Ruger Baran', 'Ryoma Nishiki', 'Ryoma Nishiki (Chrono Storm)', 'Ryoma Sakamoto',
    ### S ###
    'Sam Kincaid', 'Sam Kincaid (Emperadores)', 'Samguk Han', 'Sael', 'Seymour Hillman', 'Schemer Guile', 'Scotty', 'Scotty (Inazuma Japón)',
    'Shadow Cimmerian', 'Shadow Cimmerian (Emperadores)', 'Shawn Froste (Unido)', 
    'Shawn Froste (Adulto)', 'Shawn Froste (Aiden)', 
    'Shawn Froste (DF)', 'Shawn Froste (Legendario)', 'Shawn Froste (Orion)', 'Shishimaru', 'Shintaro Nakaoka',
    'Shun', 'Sierra', 'Sierra (MIX Z)', 'Silvia Woods', 'Simeon Ayp', 'Skie Blue', 'Soji Okita', 'Sol Daystar', 'Sol Daystar (Chrono Storm)', 
    'Sor', 'Sor (Chrono Storm)', 'Steve Grim', 'Steve Grim (Emperadores)', 'Subaru Honda', 'Sue Sparrow', 'Sue',
    ### T ###
    'Taian Inaba', 'Talisman', 'Tasuke', 'Terry Archibald', 'Tezcat', 'Thiago Torres', 'Thor Stoutberg', 'Timmy', 'Timmy (Emperadores)', 
    'Tod Ironside', 'Tod Ironside (Emperadores)', 'Tod Ironside (Inazuma Japón)', 'Tokichiro Kinoshita',
    'Thomas Feldt', 'Thomas Feldt (Emperadores)', 'Thomas Murdock',
    'Torch', 'Tori', 'Trina Verdure', 'Tyler Murdock', 'Tyler Murdock (Neo Japón)', 
    ### V ###
    'Victor Blade', 'Victor Blade (Chrono Storm)', 'Víctor Blade (Earth Eleven)', 'Víctor Blade (Falam Medium)', 'Victor García', 'Vento Gaillano', 'Vladimir Blade', 
    ### W ###
    'Wanli Changcheng', 'Walter Mountain', 'Wenel', 'William Glass', 'William Glass (Inazuma Japón)', 'William Toddsforth', 'Wittz', 'Wittz (Neo Japón)',
    'Wolfe Whyte',
    ### X ###
    'Xavier Foster', 'Xavier Schiller', 'Xavier Schiller (Ares)', 'Xene', 
    ### Y ###
    'Yasir Haddad',
    ### Z ###
    'Zack Avalon', 'Zanark Avalonic', 'Zanark Avalonic (Cao Cao)', 'Zanark Avalonic (Chrono Storm)', 'Zanos', 'Zaphod Riker', 
    'Zell', 'Zell (Neo Japón)','Zephyr Vitesse', 'Zhuge Liang', 'Zippy Lerner', 'Zohen', 'Zohen (Neo Japón)',
]
