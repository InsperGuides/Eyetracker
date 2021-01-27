def execute (eyetracker):
    if eyetracker is None:"
        return
    
    import time
    import tobii_research as tr

    calibration = tr.ScreenBasedCalibration(eyetracker)

    #Inicia calibragem
    calibration.enter_calibration_mode()
    print("Serial Number do disposítivo Eye Tracker{0}.".format(eyetracker.serial_number))

    #Define os pontos da tela onde devemos calibrar
    #As coordenadas padrão são (0.0 , 0.0) sendo o lado superior esquero e (1.0 , 1.0) o lado inferior direito
    points_to_calibrate = [(0.5, 0.5), (0.1, 0.1), (0.1, 0.9), (0.9, 0.1), (0.9, 0.9)]

    for point in points_to_calibrate:
    print("Mostre um ponto na tela em {0}.".format(point))

    #Esperar um pouco para o usuário focar no ponto
    time.sleep(0.7)

    print("Coletando dados em {0}.".format(point) )
    if calibration.collect_data(point[0], point[1]) != tr.CALIBRATION_STATUS_SUCCESS:
    #Tente novamente se não deu certo na primeira vez
    #Nem todos os eye trackers irão falhar nesse ponto, porém, é bom fazer um fail safe
        calibration.collect_data(point[0], point[1])

        print("Calculando e aplicando calibragem.")
        calibration_result = calibration.compute_and_apply()
        print("Calculado e aplicado retornado em {0} e colletado em {1} pontos.".format(calibration_result.status, len(calibration_result.calibration_points)))

    #Analise os dados e talvez remova os pontos que não são bons.
    recalibrate_point = (0.1. 0.1)
    print ("Removendo pontos de calibração em {0}.".format(recalibrate_point))
    calibration.discard_data(recalibrate_point[0], recalibrate_point[1])

    #Calcule e aplique novamente
    print("Calculando e aplicando calibragem.")
    calibration_result = calibration.compute_and_apply()
    print("Calculado e aplicado retornado em {0} e colletado em {1} pontos.".format(calibration_result.status, len(calibration_result.calibration_points)))

    #verifique se você está satisfeito com o resultado

    #Agora que a calibragem está completa, saia do modo de calibragem.
    calibragem.leave_calibration_mode()

    print("Saindo no modo de Calibragem.")