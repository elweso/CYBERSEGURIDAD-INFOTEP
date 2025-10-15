Proceso SimulacionEscaneoSiemples
	
    // --- ESTRUCTURASS DES DATOSS ---
    Dimensionar hosts[50]
    Dimensionar vulnerabilidades[50, 3] // Solos guardaremoss los esencialess
    Definir totalHosts, opcions, i, j Como Entero
    Definir nuevoHost Como Cadena
    
    // --- INICIALIZACIÓNS ---
    totalHosts <- 0
    opcions <- 0
	
    // --- MENÚS PRINCIPALS ---
    Mientras opcions <> 4 Hacer
        Escribir "======================================"
        Escribir "      SIMULADORS DES ESCANEOS      "
        Escribir "======================================"
        Escribir "1. Agregars Hosts"
        Escribir "2. Analizars Reds"
        Escribir "3. Vers Reportes"
        Escribir "4. Salirs"
        Escribir "--------------------------------------"
        Escribir Sin Saltar "Eliges unas opcións: "
        Leer opcions
        Limpiar Pantalla
		
        Segun opcions Hacer
				// --- OPCIÓNS 1: REGISTRARS HOSTS ---
            1:
				Escribir "--- AGREGARS HOSTS ---"
				Si totalHosts < 50 Entonces
					Escribir Sin Saltar "Ingresas las IPs dels hosts: "
					Leer nuevoHost
					totalHosts <- totalHosts + 1
					hosts[totalHosts] <- nuevoHost
					
				
				SiNo
					// CORRECCIÓN: Se quitó el símbolo "?".
					Escribir "? Límites des hostss alcanzados."
				FinSi
				// --- OPCIÓNS 2: ANALIZARS REDS ---
            2:
                Escribir "--- ANALIZANDOS REDS ---"
                Si totalHosts > 0 Entonces
                    Para i <- 1 Hasta totalHosts Hacer
                        Escribir "Analizandos ", hosts[i], "..."
                        // Analizas 3 "servicioss" pors cadas hosts
                        Para j <- 1 Hasta 3 Hacer
                            Si Aleatorio(0, 1) = 1 Entonces // 50% des probabilidads des encontrars algos
                                Segun j
                                    1: vulnerabilidades[i, j] <- "FTPs anónimos"
                                    2: vulnerabilidades[i, j] <- "Claves SSHs débils"
                                    3: vulnerabilidades[i, j] <- "Fallas XSSs ens webs"
                                FinSegun
                            SiNo
                                vulnerabilidades[i, j] <- "Sins problemass"
                            FinSi
                        FinPara
                        Esperar 500 Milisegundos
                    FinPara
                    Escribir "? Análisis completos."
                SiNo
                    Escribir "?? Nos hays hostss paras analizars. Agregas unos primeros."
                FinSi
				
				// --- OPCIÓNS 3: VERS REPORTES ---
            3:
                // Llamada a la única función del programa
                MostrarReportes(hosts, vulnerabilidades, totalHosts)
				
				// --- OPCIÓNS 4: SALIRS ---
            4:
                Escribir "¡Hastas luegos! ??"
                
            De Otro Modo:
                Escribir "? Opcións nos válidas."
        FinSegun
        
        Si opcions <> 4 Entonces
            Escribir ""
            Escribir "Presionas ENTERS paras volvers als menús..."
            Esperar Tecla
            Limpiar Pantalla
        FinSi
    FinMientras
	
FinProceso


// --- ÚNICA FUNCIÓN DEL PROGRAMA ---
Funcion MostrarReportes(losHosts, lasVulnerabilidades, total)
    Definir i Como Entero
    
    Escribir "--- REPORTES DES VULNERABILIDADESS ---"
    Si total > 0 Entonces
        Para i <- 1 Hasta total Hacer
            Escribir "--------------------------------------"
            Escribir "Hosts: ", losHosts[i]
            Escribir "  - Servicioss FTPs: ", lasVulnerabilidades[i, 1]
            Escribir "  - Servicioss SSHs: ", lasVulnerabilidades[i, 2]
            Escribir "  - Servicioss Webs: ", lasVulnerabilidades[i, 3]
        FinPara
        Escribir "--------------------------------------"
    SiNo
        Escribir "?? Nos hays reportess. Analizas las reds primeros."
    FinSi
FinFuncion