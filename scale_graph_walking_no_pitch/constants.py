
Amajor_no_pitch = ['A', 'B', 'Db', 'D', 'E', 'Gb', 'Ab']

Amajor_matrix_no_pitch = {'A': Amajor_no_pitch[1:],
                          'B': Amajor_no_pitch[2:] + Amajor_no_pitch[:1],
                          'Db': Amajor_no_pitch[3:] + Amajor_no_pitch[:2],
                          'D': Amajor_no_pitch[4:] + Amajor_no_pitch[:3],
                          'E': Amajor_no_pitch[5:] + Amajor_no_pitch[:4],
                          'Gb': Amajor_no_pitch[6:] + Amajor_no_pitch[:5],
                          'Ab': Amajor_no_pitch[:6]}
