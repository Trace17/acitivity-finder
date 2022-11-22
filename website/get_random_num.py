import time

def get_random_num(num_of_results):
    input_file = open("/Users/tracesweeney/Documents/OSU_CS/CS361/date_finder/BA_microservice/result_receiver.txt", "r+")
    input_file.truncate()
    input_file.close()
    output_file = open("/Users/tracesweeney/Documents/OSU_CS/CS361/date_finder/BA_microservice/random_activity.txt", "r+")
    output_file.truncate()
    output_file.close()
    input_file = open("/Users/tracesweeney/Documents/OSU_CS/CS361/date_finder/BA_microservice/result_receiver.txt", "w")
    input_file.write(str(num_of_results))
    input_file.close
    input_file = open("/Users/tracesweeney/Documents/OSU_CS/CS361/date_finder/BA_microservice/result_receiver.txt", "w")
    input_file.close()
    input_file = open("/Users/tracesweeney/Documents/OSU_CS/CS361/date_finder/BA_microservice/result_receiver.txt", "r")
    input_file.close()
    time.sleep(1)
    output_file = open("/Users/tracesweeney/Documents/OSU_CS/CS361/date_finder/BA_microservice/random_activity.txt")
    output_file_contents = output_file.read()
    output_file.close()
    input_file = open("/Users/tracesweeney/Documents/OSU_CS/CS361/date_finder/BA_microservice/result_receiver.txt", "r+")
    input_file.truncate()
    return output_file_contents