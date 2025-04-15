import unittest
from TemperatureLog import TemperatureLog

test_cases = [
    (
        [(5.481, 9.834), (2.411, 7.977), (0.977, 9.435), (0.302, 4.309), (8.982, 2.019), (8.833, 7.974), (1.482, 0.381), (0.822, 7.606), (7.562, 8.19), (1.074, 7.911)],
        [(4, 1, 0.0)]
    ),
    (
        [(8.152, 9.648), (11.768, 15.478), (4.915, 18.909), (6.544, 16.42), (0.912, 14.565), (19.589, 13.193), (17.566, 6.106), (14.04, 0.992), (1.91, 18.539), (19.265, 4.319), (6.477, 8.815), (2.827, 3.101), (3.685, 5.109), (15.497, 0.253), (8.97, 5.518), (12.381, 16.006), (9.577, 4.924), (11.415, 4.853), (4.297, 17.488), (12.465, 16.38)],
        [(1, 2, 12.0683), (8, 2, 9.065)]
    ),
    (
        [(33.63, 31.327), (9.302, 22.348), (18.1, 35.923), (9.333, 1.439), (39.461, 1.077), (11.783, 2.158), (6.375, 39.878), (19.351, 37.902), (19.211, 15.616), (39.741, 27.875), (20.329, 6.395), (6.927, 46.454), (19.182, 5.545), (19.778, 44.611), (15.851, 33.042), (42.821, 42.002), (5.547, 23.983), (21.232, 2.701), (48.405, 46.257), (39.528, 37.311), (17.513, 38.74), (26.073, 17.696), (10.232, 20.747), (31.304, 40.015), (39.986, 46.468), (2.127, 12.259), (15.313, 5.793), (24.482, 3.252), (47.204, 27.286), (46.723, 38.584), (21.395, 24.935), (26.313, 7.173), (4.224, 18.069), (11.004, 48.299), (4.819, 45.692), (33.524, 35.589), (25.977, 42.486), (0.568, 15.605), (4.852, 34.833), (14.982, 41.982), (13.023, 45.028), (35.55, 0.536), (24.698, 48.658), (3.892, 36.536), (5.655, 25.544), (15.761, 2.502), (21.826, 4.368), (32.524, 27.864), (3.222, 21.633), (14.291, 32.325)],
        [(11, 11, 24.7776), (39, 7, 27.7832), (32, 11, 24.5185), (48, 7, 38.5322), (49, 2, 36.7715)]
    ),
    (
        [(56.73, 0.654), (74.212, 77.809), (10.206, 91.835), (66.667, 99.794), (3.021, 28.322), (6.091, 20.966), (2.028, 31.196), (25.941, 35.188), (18.971, 40.049), (30.634, 28.526), (13.249, 73.305), (18.267, 69.92), (16.705, 69.672), (86.723, 93.399), (57.007, 66.534), (66.694, 5.246), (98.533, 6.836), (45.333, 15.064), (10.5, 46.407), (31.319, 14.944), (2.737, 32.471), (89.495, 9.282), (4.221, 22.35), (94.142, 51.94), (85.376, 22.641), (6.818, 94.146), (90.305, 62.512), (39.327, 74.646), (76.653, 42.463), (7.331, 91.053), (56.663, 36.949), (76.872, 25.761), (91.612, 79.433), (74.803, 13.438), (28.652, 39.708), (77.054, 24.229), (78.011, 98.718), (56.045, 37.864), (52.982, 12.058), (75.216, 7.39), (95.054, 28.738), (71.888, 20.077), (91.911, 88.036), (12.149, 64.269), (12.634, 41.344), (26.997, 51.362), (51.059, 16.766), (93.612, 70.116), (9.164, 43.665), (11.725, 81.071), (66.813, 30.551), (30.739, 84.653), (80.428, 79.75), (61.85, 63.492), (86.65, 34.494), (39.013, 68.116), (92.709, 46.976), (93.722, 74.745), (81.76, 36.901), (25.479, 66.158), (68.872, 39.385), (98.431, 84.008), (46.103, 2.298), (90.116, 11.819), (86.45, 21.074), (38.862, 36.734), (19.274, 26.168), (55.873, 16.62), (87.819, 1.204), (3.144, 75.901), (68.788, 9.17), (51.424, 63.257), (59.275, 91.334), (7.494, 33.784), (46.163, 97.996), (48.773, 25.596), (65.588, 97.116), (12.224, 29.443), (29.596, 24.877), (83.87, 41.523), (94.948, 1.047), (53.298, 37.389), (65.101, 48.416), (19.563, 45.12), (55.248, 89.219), (85.012, 76.278), (39.926, 45.576), (56.413, 35.468), (58.896, 93.265), (33.04, 99.944), (45.793, 55.018), (74.627, 85.771), (14.193, 89.236), (47.736, 0.433), (55.196, 72.531), (45.782, 58.16), (58.592, 93.55), (10.396, 55.567), (14.507, 1.88), (90.445, 19.044)],
        [(61, 25, 47.6877), (79, 22, 49.4387), (70, 9, 46.4015), (58, 20, 46.0286), (87, 6, 42.9744), (37, 5, 65.0032), (79, 8, 47.1597), (64, 10, 52.3617), (31, 25, 49.8241), (62, 5, 68.9298)]
    ),
    (
        [(77.542, 43.261), (8.757, 99.947), (61.195, 15.765), (5.689, 49.711), (80.262, 65.903), (78.886, 69.066), (57.902, 50.198), (73.89, 96.952), (32.736, 77.586), (71.034, 51.283), (54.793, 36.448), (49.144, 53.046), (72.935, 46.76), (75.042, 23.07), (70.766, 23.83), (36.791, 39.358), (25.988, 86.629), (53.224, 86.336), (32.503, 25.468), (53.942, 64.952), (26.792, 9.976), (0.257, 2.206), (94.088, 32.32), (28.886, 13.21), (49.941, 20.276), (47.922, 48.396), (84.623, 66.337), (69.133, 64.518), (27.53, 2.222), (53.84, 0.855), (29.011, 49.249), (16.308, 23.809), (98.811, 71.075), (25.547, 4.699), (19.572, 50.352), (39.323, 26.679), (9.684, 37.208), (72.256, 48.074), (2.178, 99.243), (36.589, 50.973), (50.44, 96.465), (8.8, 11.601), (88.773, 85.558), (9.181, 56.25), (49.28, 80.987), (18.861, 76.55), (77.023, 33.501), (23.059, 15.446), (49.387, 94.756), (33.13, 87.535), (33.918, 46.587), (67.551, 29.069), (52.41, 41.407), (97.772, 50.601), (71.01, 33.056), (39.166, 4.749), (92.155, 3.15), (29.661, 87.755), (28.624, 35.365), (61.243, 28.959), (50.208, 63.541), (16.167, 90.111), (32.399, 13.7), (11.289, 88.067), (26.762, 85.016), (58.234, 37.724), (69.697, 81.274), (45.534, 99.058), (77.649, 47.554), (24.621, 31.355), (46.858, 52.863), (87.912, 49.141), (13.184, 75.593), (46.528, 46.435), (19.854, 75.079), (79.355, 88.994), (2.327, 22.404), (74.747, 50.566), (81.532, 86.383), (39.648, 90.008), (90.649, 89.453), (2.274, 64.469), (49.276, 48.641), (99.673, 77.602), (14.748, 36.204), (8.674, 70.183), (98.17, 39.058), (66.886, 92.88), (89.874, 8.355), (18.739, 90.998), (82.225, 47.391), (65.29, 91.715), (5.005, 16.589), (37.812, 45.675), (32.147, 57.554), (93.976, 66.05), (8.918, 71.632), (22.748, 0.14), (53.238, 52.278), (23.419, 29.536), (79.603, 16.429), (45.246, 87.825), (32.233, 35.039), (31.14, 6.307), (26.609, 95.651), (89.721, 55.038), (34.98, 21.067), (12.475, 19.208), (40.472, 43.317), (42.892, 71.561), (88.801, 91.092), (19.508, 99.127), (94.997, 24.576), (53.308, 94.688), (71.03, 94.738), (8.726, 35.677), (35.844, 44.052), (12.62, 51.8), (96.693, 44.847), (24.795, 50.434), (83.931, 11.661), (13.92, 90.665), (95.564, 77.371), (83.507, 53.264), (43.216, 88.974), (71.823, 0.11), (61.24, 42.306), (64.383, 49.031), (65.444, 62.964), (49.778, 83.533), (13.551, 7.264), (36.905, 49.614), (62.295, 3.227), (31.376, 57.862), (39.188, 43.162), (35.364, 3.888), (10.595, 53.683), (95.488, 24.647), (66.061, 96.298), (23.445, 34.827), (13.813, 86.84), (82.779, 65.765), (2.544, 8.661), (15.305, 25.501), (59.342, 86.898), (70.325, 70.113), (58.837, 27.615), (25.428, 11.522), (58.952, 63.367), (90.952, 52.391), (19.063, 37.867), (33.496, 91.627), (53.595, 5.249), (77.255, 67.116), (98.172, 67.257), (4.533, 4.427), (91.666, 69.463), (36.46, 84.804), (54.239, 49.33), (39.585, 89.642), (79.724, 3.857), (12.8, 93.243), (36.753, 46.155), (96.966, 3.987), (34.458, 85.283), (61.178, 66.921), (30.512, 52.523), (69.545, 72.342), (75.288, 44.901), (68.655, 94.973), (96.28, 57.957), (23.739, 75.721), (80.517, 23.411), (87.16, 37.422), (18.925, 64.132), (94.152, 68.977), (40.04, 49.675), (66.194, 80.954), (16.755, 44.494), (27.956, 48.508), (79.137, 5.21), (26.182, 7.892), (99.569, 51.017), (59.776, 77.717), (45.781, 77.564), (52.149, 32.485), (27.182, 30.454), (26.588, 32.359), (33.886, 30.816), (49.278, 83.475), (41.268, 96.338), (26.979, 24.23), (9.045, 18.391), (53.314, 74.203), (14.59, 17.159), (19.168, 42.092), (63.177, 65.643), (62.48, 28.106), (52.042, 75.255), (87.057, 2.108), (48.708, 92.264), (80.844, 31.128), (63.886, 82.702), (39.3, 41.176), (28.75, 87.532), (68.414, 33.214), (49.818, 92.817), (33.01, 81.117), (80.893, 6.738), (19.887, 99.184), (29.423, 31.341), (58.099, 39.204), (92.402, 52.003), (43.221, 34.094), (25.718, 0.514), (9.844, 4.954), (81.107, 64.875), (96.522, 65.949), (11.981, 37.694), (7.747, 20.187), (57.061, 75.519), (73.305, 24.144), (67.179, 77.172), (43.514, 38.05), (78.491, 17.995), (7.007, 17.94), (91.838, 65.907), (69.601, 7.396), (72.42, 35.319), (11.655, 83.893), (15.157, 75.025), (27.152, 2.919), (25.877, 30.338), (13.512, 43.015), (80.209, 65.08), (26.682, 95.179), (28.341, 58.36), (53.725, 33.769), (37.266, 59.714), (60.229, 16.191), (41.962, 32.392), (73.393, 46.184), (46.031, 76.195), (99.191, 83.638), (96.474, 76.57), (95.527, 27.852), (77.981, 14.266), (93.366, 76.91), (62.249, 87.661), (69.909, 20.51), (16.324, 94.765), (59.407, 9.638), (34.768, 44.635), (63.75, 75.885), (34.692, 5.641), (62.171, 50.056), (13.147, 49.586), (83.949, 28.846), (5.809, 97.955), (83.813, 22.029), (58.409, 12.51), (80.199, 66.671), (8.071, 65.232), (1.854, 84.565), (35.312, 27.587), (16.315, 6.43), (84.575, 5.804), (91.114, 85.829), (25.392, 53.987), (15.235, 24.108), (0.508, 37.431), (89.918, 6.352), (38.811, 16.677), (35.571, 89.666), (25.567, 60.769), (85.254, 39.699), (13.244, 50.865), (39.797, 68.621), (22.302, 32.928), (33.386, 92.581), (13.435, 40.251), (46.517, 11.324), (27.468, 56.625), (33.548, 47.214), (85.406, 12.557), (22.192, 65.889), (15.983, 51.413), (90.061, 72.048), (16.471, 19.139), (9.528, 11.348), (35.956, 38.155), (1.4, 98.864), (43.434, 93.265), (16.759, 89.333), (30.932, 58.675), (67.311, 6.487), (42.428, 96.415), (90.911, 74.64), (80.516, 29.862), (58.028, 40.95), (6.734, 50.029), (28.614, 79.674), (51.733, 90.134), (20.239, 3.246), (65.647, 16.058), (72.487, 92.848), (36.509, 64.143), (49.225, 68.407), (98.707, 63.818), (60.544, 53.472), (99.366, 77.64), (28.44, 99.712), (54.641, 42.173), (8.632, 85.398), (21.888, 83.066), (95.751, 15.707), (71.68, 26.256), (48.282, 42.896), (43.515, 38.099), (63.032, 14.93), (78.595, 76.213), (35.75, 88.694), (79.821, 83.344), (65.742, 28.818), (85.839, 7.956), (66.483, 97.501), (64.048, 85.91), (49.273, 79.786), (48.311, 51.865), (83.482, 74.038), (55.087, 34.272), (29.207, 73.983), (56.112, 97.19), (70.019, 84.554), (54.941, 12.73), (99.403, 75.514), (25.369, 73.617), (40.267, 96.099), (56.157, 32.383), (68.14, 31.885), (49.402, 16.145), (86.277, 18.624), (26.715, 3.194), (37.417, 41.113), (25.658, 43.807), (99.583, 47.987), (65.117, 12.619), (29.721, 26.469), (97.329, 36.474), (6.872, 66.214), (81.346, 4.805), (64.383, 19.558), (54.558, 80.22), (3.452, 36.081), (28.3, 2.489), (62.416, 8.014), (67.117, 36.844), (17.095, 50.952), (86.562, 72.38), (40.414, 60.312), (92.985, 73.934), (41.424, 56.847), (97.083, 45.411), (82.337, 37.328), (29.735, 3.47), (18.188, 69.448), (8.118, 75.592), (1.147, 6.375), (52.315, 90.517), (11.239, 35.439), (54.478, 95.476), (77.159, 88.348), (79.685, 98.665), (90.54, 27.255), (92.155, 92.437), (2.784, 91.244), (34.916, 22.901), (34.922, 26.716), (75.084, 28.214), (98.915, 48.992), (76.697, 53.855), (75.991, 7.461), (87.611, 93.276), (68.078, 52.869), (39.325, 54.911), (30.185, 49.841), (2.256, 37.155), (96.822, 64.823), (25.374, 40.72), (85.975, 90.337), (0.615, 40.79), (25.011, 92.651), (54.115, 98.309), (87.14, 1.904), (4.01, 83.254), (39.071, 3.949), (54.303, 38.723), (25.582, 55.207), (58.527, 65.919), (82.717, 58.358), (73.633, 91.901), (96.431, 21.659), (51.335, 81.091), (31.246, 70.161), (24.582, 39.999), (64.2, 28.558), (48.008, 84.959), (83.796, 80.459), (3.363, 82.849), (34.918, 0.737), (46.856, 38.476), (56.449, 2.847), (46.04, 8.051), (7.166, 99.031), (70.784, 50.614), (69.937, 90.567), (87.57, 74.09), (55.957, 51.447), (90.323, 58.843), (64.187, 24.57), (22.403, 7.044), (39.247, 5.34), (91.603, 98.978), (16.785, 91.14), (11.4, 45.681), (44.016, 61.901), (26.019, 28.372), (29.685, 41.02), (95.29, 57.816), (74.749, 57.158), (22.649, 89.247), (95.091, 85.954), (56.55, 21.834), (38.039, 64.198), (59.539, 66.36), (51.965, 58.329), (47.362, 14.621), (84.523, 7.865), (61.647, 7.157), (18.577, 31.995), (55.943, 13.15), (34.066, 83.255), (78.368, 51.07), (94.253, 65.794), (43.09, 87.594), (76.256, 59.558), (48.614, 94.107), (96.294, 6.057), (5.775, 52.147), (47.29, 27.748), (39.393, 75.059), (63.331, 66.349), (64.41, 60.204), (15.511, 61.324), (35.54, 14.773), (78.182, 52.645), (22.51, 44.537), (2.655, 85.87), (27.839, 33.493), (72.838, 17.139), (68.941, 67.297), (36.698, 38.73), (10.283, 2.418), (14.504, 23.395), (81.933, 80.865), (66.449, 95.951), (93.315, 84.807), (28.932, 14.881), (12.758, 23.684), (89.574, 56.605), (34.059, 10.195), (39.949, 40.003), (3.864, 61.452), (53.093, 33.585), (20.753, 63.684), (61.793, 46.092), (96.962, 84.506), (92.753, 46.737), (66.854, 46.6), (98.011, 14.309), (61.73, 78.235), (85.678, 8.592), (56.582, 62.094), (70.088, 20.076), (28.147, 91.137), (47.836, 1.945), (80.829, 59.367), (38.715, 67.604), (30.055, 25.275), (51.033, 11.81), (23.766, 48.302), (92.97, 65.919), (5.318, 21.492), (9.208, 36.21), (15.488, 61.989), (15.275, 44.671), (36.378, 54.412), (66.362, 78.888), (70.557, 99.025), (36.178, 71.206)],
        [(19, 15, 48.9242), (96, 12, 52.0747), (73, 9, 51.7319), (88, 18, 50.7403), (94, 3, 55.9216), (67, 18, 51.2914), (44, 6, 56.9195), (4, 9, 50.0578), (46, 22, 50.6995), (14, 11, 50.5374), (88, 8, 50.5902), (86, 19, 50.7741), (53, 22, 52.589), (47, 6, 61.0789), (4, 11, 49.5922), (14, 15, 49.1197), (81, 14, 50.4366), (14, 3, 51.5085), (93, 18, 50.3702), (18, 12, 48.4476), (75, 17, 49.9165), (53, 13, 53.2541), (13, 9, 51.9906), (92, 8, 52.0747), (39, 25, 50.4243), (32, 1, 42.9596), (100, 1, 68.8996), (30, 16, 50.0067), (7, 22, 49.1197), (53, 14, 54.103), (50, 20, 52.4547), (24, 25, 49.9613), (38, 23, 51.0953), (78, 14, 50.916), (63, 20, 52.4468), (6, 23, 49.1197), (18, 6, 51.668), (87, 19, 51.124), (42, 2, 65.5354), (15, 25, 48.5395), (13, 3, 48.2647), (62, 2, 44.0879), (14, 22, 48.3937), (57, 12, 53.0423), (65, 3, 53.1631), (50, 1, 67.8365), (60, 24, 52.4809), (98, 18, 51.2354), (98, 4, 51.6988), (55, 5, 52.2748)]
    ),
]

class TestTemperatureLog(unittest.TestCase):
    def run_test(self, samples, cases):
        THRESHOLD = 0.01

        log = TemperatureLog()
        for x, y in samples:
            log.add_sample(x, y)
            
        for x, T, gold in cases:
            pred = log.predict(x, T)
            self.assertTrue(abs(pred - gold) < THRESHOLD)

    def test1(self):
        self.run_test(test_cases[0][0], test_cases[0][1])

    def test2(self):
        self.run_test(test_cases[1][0], test_cases[1][1])

    def test3(self):
        self.run_test(test_cases[2][0], test_cases[2][1])

    def test4(self):
        self.run_test(test_cases[3][0], test_cases[3][1])

    def test5(self):
        self.run_test(test_cases[4][0], test_cases[4][1])

if __name__ == '__main__':
   res = unittest.main(verbosity = 3, exit = False)
