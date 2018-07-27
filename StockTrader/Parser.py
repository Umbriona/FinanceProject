import numpy as np

# trade | change | change % | lastClose | open |  bid price | Bid volume | Ask price | Ask volume | Volume | Volume ave|
# Market cap | Beta | PE Ratio | EPS | Forward Dividend & Yield | Ex-Dividend Date | 1y Target Est | time | Date


def parse_open(file_path='E:\\Financial_data\\open\\Amd_open.txt'):
    try:
        dr = open(file_path, 'r')
    except FileNotFoundError:
        dr = open("C:\\Users\sandr\Documents\Financial_data\open\\Amd_open.txt", 'r')
    plane_text = dr.read()
    plane_text = ''.join(c for c in plane_text if c not in 'xBM()%,')
    split_n_list = plane_text.split('\n')

    data_tensor = np.zeros([21, len(split_n_list)-1])
    j = 0
    for i in split_n_list[:len(split_n_list)-1]:
        temp = i.split(' ')
        while '' in temp:
            temp.remove('')
        n = 0
        length_data = len(temp)-1
        for k in temp:
            if n != length_data-3 and n != length_data-1 and n != length_data:
                data_tensor[n, j] = float(k)
            elif n == length_data-3:
                if k == 'N/A':
                    data_tensor[n, j] = 0
                else:
                    data_tensor[n, j] = float(''.join(c for c in k if c not in '-'))
            elif n == length_data-1:
                time_split = k.split(':')
                data_tensor[n, j] = float(time_split[0]) * 3600 + float(time_split[1]) * 60 + float(time_split[2])
            else:
                z = k.split(':')
                # z = ''.join(c for c in k if c not in ':')
                data_tensor[n, j] = float(z[0])
                data_tensor[n+1, j] = float(z[1])
                data_tensor[n+2, j] = float(z[2])
            n += 1
        j += 1

    #while try np.all(data_tensor[length_data+3, :] == 0):
     #   data_tensor = np.delete(data_tensor, length_data+3, axis=0)


    return data_tensor
# lastClose | open |  bid price | Bid volume | Ask price | Ask volume | Volume | Volume ave|
# Market cap | Beta | PE Ratio | EPS | Forward Dividend & Yield | Ex-Dividend Date | 1y Target Est | time | Date


def parse_closed(file_path='E:\\Financial_data\\closed\\Amd_closed.txt'):
    dr = open(file_path, 'r')
    plane_text = dr.read()
    plane_text = ''.join(c for c in plane_text if c not in 'xBM()%,')
    split_n_list = plane_text.split('\n')

    data_tensor = np.zeros([19, len(split_n_list)-1])
    j = 0
    for i in split_n_list:
        temp = i.split(' ')
        while '' in temp:
            temp.remove('')
        n = 0
        length_data = len(temp)-1
        for k in temp:
            if n != length_data-3 and n == length_data-1 and n == length_data:
                data_tensor[n, j] = float(k)
            elif n == length_data-3:
                data_tensor[n, j] = float(''.join(c for c in k if c not in '-'))
            elif n == length_data-1:
                time_split = k.split(':')

                data_tensor[n, j] = float(time_split[0]) * 3600 + float(time_split[1]) * 60 + float(time_split[2])
            else:
                z = ''.join(c for c in k if c not in ':')
                data_tensor[n, j] = float(z)
            n += 1
        j += 1

    return data_tensor

parse_open()