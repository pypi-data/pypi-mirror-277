import math
import os
import subprocess

import cv2
# 主要是需要moviepy这个库
from moviepy.editor import VideoFileClip, concatenate_videoclips


class VideoOperation(object):
    def __init__(self,ffmpeg_path,ffprobe_path):
        # project_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
        # self.ffmpeg = os.path.join(project_path, "media", 'ffmpeg-20160705-ce466d0-win64-static', "bin",
        #                            "ffmpeg.exe")
        # self.ffprobe = os.path.join(project_path, "media", 'ffmpeg-20160705-ce466d0-win64-static', "bin",
        #                             "ffprobe.exe")
        self.ffmpeg = ffmpeg_path
        self.ffprobe = ffprobe_path

    def create_m3u8_2(self, video, m3u8, ts_time=9, ffmpeg=None):
        if not ffmpeg:
            ffmpeg = self.ffmpeg
        ts_filename = m3u8
        cmd = f"{ffmpeg} -i {video} -c:v libx264 -c:a aac -strict -2 -f hls -hls_list_size 2 -hls_time {ts_time} {ts_filename}.m3u8 -loglevel quiet"
        # 调用subprocess运行命令
        # subprocess.call(mp4ToTs, shell=True)
        # subprocess.call(tsToM3u8, shell=True)
        subprocess.call(cmd, shell=True)

    def create_m3u8_1(self, video, m3u8, ts_time=9, ffmpeg=None):
        if not ffmpeg:
            ffmpeg = self.ffmpeg
        # video = "2022-03-27-14-15.mp4"
        # m3u8 = "m3u8/ccs/3s.m3u8"
        # ts_time = 9
        cmd = f"{ffmpeg} -i {video} -c:v libx264 -hls_time {ts_time} -hls_list_size 0 -c:a aac -strict -2 -f hls {m3u8} -loglevel quiet"
        # cmd1 = f"""{ffmpeg} -i {video} -force_key_frames "expr:gte(t,n_forced*{ts_time})" -strict -2 -c:a aac -c:v libx264 -hls_time {ts_time} -f hls {m3u8}"""
        # print(cmd1)

        os.system(cmd)

        return m3u8

    def create_m3u8(self, video, m3u8, ts_time=9, ffmpeg=None):
        if not ffmpeg:
            ffmpeg = self.ffmpeg
        # video = "2022-03-27-14-15.mp4"
        # m3u8 = "m3u8/ccs/3s.m3u8"
        # ts_time = 9
        # root_path为ffmpeg的路径，file_name_path为mp4文件路径，ts_filename转换为ts的文件名
        ts_filename = m3u8
        mp4ToTs = ffmpeg + " -y -i " + video + " -vcodec copy -acodec copy -vbsf h264_mp4toannexb " + ts_filename + ".ts -loglevel quiet"
        # 把ts转换成m3u8列表，-segment_time 10 参数表示约10秒一段视频，ts_filename为m3u8文件列表的文件名
        tsToM3u8 = ffmpeg + " -i " + ts_filename + f".ts -c copy -map 0 -f segment -segment_time {ts_time} -segment_list " + ts_filename + ".m3u8 " + ts_filename + "%03d.ts -loglevel quiet"
        # 调用subprocess运行命令
        subprocess.call(mp4ToTs, shell=True)
        subprocess.call(tsToM3u8, shell=True)

    # create_m3u8('F:\录屏\虚拟.mp4', 'd/q.m3u8', 1)
    def ts_png(self, ts, png, ffmpeg=None):
        if not ffmpeg:
            ffmpeg = self.ffmpeg
        cmd = f"{ffmpeg} -i {ts} -r 1/1 {png} "
        os.system(cmd)

    def get_relatively_codec(self, codec):
        if codec == 'hevc' or codec == "h265":
            return 'libx265'
        elif codec == 'avc' or codec == 'h264':
            return 'libx264'
        return codec

    def remove_file(self, file):
        if os.path.exists(file):
            os.remove(file)

    # 寻找文件
    def absolute_location_num_file_sort(self, dir_path, endswith, absolute=True):
        """
        :param path:文件位置
        :param endswith: 文件以什么结尾比如py，xls,word,txt等
        :param absolute: True是返回绝对路径，Flase是返回相对路径
        :return: 列表内都是文件的绝对路径
        """
        rootpath = os.listdir(dir_path)

        def get_x(x):
            try:
                return int(x[:2])
            except:
                return int(x[:1])

        rootpath.sort(key=lambda x: get_x(x) if x.endswith(endswith) or x.endswith("avi") else False)

        def is_index(n):
            if n.endswith(endswith) or n.endswith("avi"):
                return n

        rootpath = list(filter(is_index, rootpath))
        if absolute:
            rootpath = [dir_path + '\\' + i for i in rootpath]
        return rootpath

    # <editor-fold desc="合并视频文件">
    def merge_video_files_operation1(self, video_dir, target_file='target.mp4'):
        vide0_lis = self.absolute_location_num_file_sort(video_dir, 'mp4')
        with open(target_file, 'wb+') as fv:
            for index, file in enumerate(vide0_lis):
                fr = open(file, 'rb')
                fv.write(fr.read())
                fr.close()

    def merge_video_files_operation2(self, video_dir, target_file='target.mp4'):
        L = []
        vide0_lis = self.absolute_location_num_file_sort(video_dir, 'mp4')
        for index, file in enumerate(vide0_lis[:]):
            video = VideoFileClip(file)
            L.append(video)
        final_clip = concatenate_videoclips(L)
        # 生成目标视频文件
        # final_clip.to_videofile(f"{video_dir}/target.mp4", fps=24, remove_temp=False)
        final_clip.to_videofile(target_file, fps=30, remove_temp=False)

    # </editor-fold>
    # <editor-fold desc="将现成的大内存avi转换为小内存的mp4文件">
    def avi_to_mp4(self, video_path, ffmpeg=None):
        if not ffmpeg:
            ffmpeg = self.ffmpeg
        command = fr'{ffmpeg} -i {video_path}'
        subprocess.call(command.split())

    # </editor-fold>
    # <editor-fold desc="视频提取音频 ">
    # mp4_to_wav
    def mp4_to_wav(self, video_path, wav_path, ffmpeg=None):
        if not ffmpeg:
            ffmpeg = self.ffmpeg
        """
        MP3文件和WAV文件都是数字音频格式，由于两者的压缩比例和编码上面的差异，
        因此但是两者在文件大小和音质上有所不同。WAV是最接近无损的音乐格式，
        MP3文件通过对音频进行编码，去掉了某些部分，从而节省了空间。
        使用 -f wav 输出wav格式音频文件：
        :param video_path:
        :param wav_path:
        :param ffmpeg:
        :return:
        """

        # Set the path of input and output files.

        # Check if the output file exists. If so, delete it.
        if os.path.isfile(wav_path) is True:
            os.remove(wav_path)
        # Set the command for processing the input video/audio.
        cmd = f"{ffmpeg} -i " + video_path + " -ab 160k -ac 2 -ar 44100 -vn " + wav_path

        # Execute the (Terminal) command within Python.
        subprocess.call(cmd, shell=True)

    def mp4_to_mp3(self, INPUT_VIDEO, OUTPUT_FILE, order=1, ffmpeg=None):
        """
        试了一下提取mp3文件比提取wav文件慢一些，也不清楚两种提取mp3文件的方法有什么区别
         -i   输入文件，test.mp4 为原始视频文件；
         -vn  表示no video，输出不包含视频
         -f   输出文件格式
        :param INPUT_VIDEO:test.mp4
        :param OUTPUT_FILE:output.mp3
        :param ffmpeg:
        :return:
        命令
        """
        if not ffmpeg:
            ffmpeg = self.ffmpeg
        if order == 1:
            cmd = f"""{ffmpeg} -i {INPUT_VIDEO} -vn -f mp3 {OUTPUT_FILE}"""
        elif order == 2:
            cmd = f"""{ffmpeg} -i {INPUT_VIDEO} -vn -c:a mp3 {OUTPUT_FILE}"""
        else:
            raise ValueError("Unknown order")
        subprocess.call(cmd, shell=True)

    # <editor-fold desc="批量提取文件夹下多个视频文件的音频">
    def many_mp4_to_wav_bat(self, ffmpeg=None):
        """
        批量提取文件夹下多个视频文件的音频
    在该目录下创建一个批处理文件（例如 music.bat）
    在批处理文件中添加以下命令：
        :param ffmpeg:
        :return:
        """
        if not ffmpeg:
            ffmpeg = self.ffmpeg
        cmd = f"""for %%a in (*.mp4) do {ffmpeg} -i %%a -vn -f wav %%~na.wav"""
        with open('cmd.bat', 'a', encoding='utf-8') as f:
            f.write(cmd)

    # </editor-fold>

    # </editor-fold>
    # <editor-fold desc="添加**音频到视频">

    def mp4wav_to_wav(self, INPUT_VIDEO, INPUT_AUDIO, OUTPUT_FILE, ffmpeg=None):

        if not ffmpeg:
            ffmpeg = self.ffmpeg
        # Set the path of input and output files.
        # INPUT_VIDEO = "Media/Demo_1080P.mp4"
        # INPUT_AUDIO = "Media/Demo.wav"
        # OUTPUT_FILE = "Media/Demo_1080P_S.mp4"
        # Check if the output file exists. If so, delete it.
        if os.path.isfile(OUTPUT_FILE) is True:
            os.remove(OUTPUT_FILE)
        # Set the command for processing the input video/audio.
        cmd = f"{ffmpeg} -i " + INPUT_VIDEO + " -i " + INPUT_AUDIO + " -c:v copy -c:a aac -strict experimental " + OUTPUT_FILE
        # Execute the (Terminal) command within Python.
        subprocess.call(cmd, shell=True)

    # </editor-fold>
    # 转换**音频的格式。
    def wav_mp3(self, INPUT_AUDIO, OUTPUT_FILE, ffmpeg=None):
        if not ffmpeg:
            ffmpeg = self.ffmpeg
        # Set the path of input and output files.
        # INPUT_AUDIO = "Media/Demo.wav"
        # OUTPUT_FILE = "Media/Demo.mp3"
        # Check if the output file exists. If so, delete it.
        if os.path.isfile(OUTPUT_FILE) is True:
            os.remove(OUTPUT_FILE)
        # Set the command for processing the input video/audio.
        cmd = f"{ffmpeg} -i " + INPUT_AUDIO + " -ab 160k -ac 2 -ar 44100 -vn " + OUTPUT_FILE

        # Execute the (Terminal) command within Python.
        subprocess.call(cmd, shell=True)

    # 删除**视频中的音频。
    def mp4s_to_mp4(self, INPUT_VIDEO, OUTPUT_FILE, ffmpeg=None):
        if not ffmpeg:
            ffmpeg = self.ffmpeg
        # Set the path of input and output files.
        # INPUT_VIDEO = "Media/Demo_360P.mp4"
        # OUTPUT_FILE = "Media/Demo_360P_noS.mp4"
        # Check if the output file exists. If so, delete it.
        if os.path.isfile(OUTPUT_FILE) is True:
            os.remove(OUTPUT_FILE)
        # Set the command for processing the input video/audio.
        cmd = f"{ffmpeg} -y -i " + INPUT_VIDEO + " -an -vcodec copy " + OUTPUT_FILE
        # Execute the (Terminal) command within Python.
        subprocess.call(cmd, shell=True)

    # <editor-fold desc="视频转图片">
    def video_to_image(self, video_path):
        # ts = r'F:\jiyiproj\jy_reconsitutionproj\WaterSystem\new_2\mysqlpro\WaterSystemCarMounted\extra_frame\Hikvision\aaaa\1656324426.ts'
        # ts = r"F:\jiyiproj\jy_reconsitutionproj\WaterSystem\new_2\mysqlpro\WaterSystemCarMounted\extra_frame\Hikvision\aaaa\1656321598.ts"
        # cap = cv2.VideoCapture('video/MOV_0005.MOV')  # 加载视频文件
        # cap = cv2.VideoCapture('Pic2Video.mp4')  # 加载视频文件
        cap = cv2.VideoCapture(video_path)  # 加载视频文件
        cap_num = cap.get(7)  # 获取视频总帧数
        cap_width = math.ceil(cap.get(3))  # 获取视频帧宽度（横）
        cap_height = math.ceil(cap.get(4))  # 获取视频帧高度（竖）
        cap_fps = math.ceil(cap.get(5))  # 获取视频帧率
        print(cap_height, cap_width, cap_fps, cap_num, "获取视频帧率")  # (1284 1236 1)
        # 得到视频总帧数的位数，比如198帧（三位数），得到3；1989帧（4位数），得到4
        # cap_count = 0
        # while cap_num:
        #     cap_count = cap_count + 1
        #     cap_num = math.floor(cap_num / 10)
        # fix = '%0' + str(cap_count) + 'd'  # 得到图片保存的前缀，比如001.png，0001.png
        # print(fix)
        # cap_cnt = 1
        # flag, frame = cap.read()  # 读取图片
        # while flag:
        #     path = 'video/' + str(fix % cap_cnt) + '.png'  # 图片保存目录
        #     # path = str(fix % cap_cnt) + '.png'  # 图片保存目录
        #     cv2.imwrite(path, frame)
        #     cap_cnt = cap_cnt + 1
        #     flag, frame = cap.read()
        # cap.release()

    # </editor-fold>
    # 使用ffmpeg从视频文件中提取视频帧
    def video_to_jpg(self, INPUT_VIDEO, OUTPUT_DIR='.', order=1, ffmpeg=None):
        """
        上面两个指令都可以
        其中 -r 8 和 -vf fps=fps=8 均表示按 fps = 8 进行抽帧
        得到的结果如下图所示，但是我是将10s的视频进行提取，
        按理说应该是10*8=80帧，但是最终刚得到的是86张图片，
        这个10s的视频是按照下面的方法将大视频按照固定时长（10s）切割成小片段得到的，
        不太清楚这是怎么回事。
        :param INPUT_AUDIO:test.mp4
        :param OUTPUT_FILE:output.mp3
        :param ffmpeg:
        :return:
        命令
        """
        if not ffmpeg:
            ffmpeg = self.ffmpeg
        if order == 1:
            cmd = f"""{ffmpeg} -i {INPUT_VIDEO} -r 8 -f image2 {OUTPUT_DIR}/%05d.jpg"""
        elif order == 2:
            cmd = f"""{ffmpeg} -i {INPUT_VIDEO} -vf fps=8 -f image2 {OUTPUT_DIR}/%05d.jpg"""
        else:
            raise ValueError("Unknown order")
        subprocess.call(cmd, shell=True)

    def clip_video(self, source_file, start_time, end_time):
        """
        利用moviepy进行视频剪切
        :param source_file: 原视频的路径，mp4格式
        :param target_file: 生成的目标视频路径，mp4格式
        :param start_time: 剪切的起始时间点（第start_time秒）
        :param stop_time: 剪切的结束时间点（第stop_time秒）
        :return:
        start_time = 90
    end_time = 60 * 5  # + start_time
    vide0_lis = ['G:\电影\亮剑.mp4', ]
    clip_video(vide0_lis[0], start_time, end_time)
        """
        source_video = VideoFileClip(source_file)
        duration = source_video.duration
        fps = source_video.fps
        print(duration, source_video.fps, source_video.start)
        time_list = [i for i in range(start_time, 2730, end_time)]
        time_list.append(duration)
        print(time_list)
        d1 = source_file.split('\\')[-1].split('.')[0]
        if not os.path.exists(os.path.join("剪辑", d1)):
            os.makedirs(os.path.join("剪辑", d1))
        for index in range(len(time_list) - 1):
            video = source_video.subclip(int(time_list[index]), time_list[index + 1])  # 执行剪切操作
            print(int(time_list[index]), time_list[index + 1], video)
            video.write_videofile(f'{os.path.join("剪辑", d1)}/{index + 1}.mp4', fps=fps)  # 输出文件

    # 压缩视频文件
    def compress_video(self, INPUT_VIDEO, OUTPUT_FILE, codec=None, crf: int = None, fps: int = None,
                       scale: list = None, bitrate=None, start_time: int = None, progress=None, ffmpeg=None):
        self.remove_file(OUTPUT_FILE)
        if not ffmpeg:
            ffmpeg = self.ffmpeg
        """
        -crf 23 指定了视频的压缩质量，数值范围一般在 18 到 28 之间，18 为最高质量，28 为最低质量。
        ffmpeg -i input.mp4 -vf scale=640:-2 -r 30 output.mp4
        在这个命令中，-vf scale=640:-2 表示将视频分辨率缩放为宽度为640像素，高度按比例缩放。
        -r 30 表示将视频帧率设置为30帧/秒。你可以根据自己的需求调整分辨率和帧率的值。
        如果你想同时压缩视频的码率，可以添加 -b:v 参数，例如：
        ffmpeg -i input.mp4 -vf scale=640:-2 -r 30 -b:v 1M output.mp4
        在这个命令中，-b:v 1M 表示将视频的码率设置为1Mbps。你可以根据自己的需求调整码率的值。
        在这个示例中，-c:v libx264参数指定了视频编码器为H.264，-crf 23参数指定了视频的质量，数值越小表示质量越高，-c:a aac -b:a 128k参数指定了音频编码器为AAC，比特率为128k。
        你也可以根据需要调整其他参数，比如分辨率、帧率等，来进一步压缩视频文件。请注意，视频压缩会损失一定的画质，因此需要根据实际需求来进行调整。
        希望这可以帮助到你。如果你有任何其他问题，欢迎随时问我。
        """
        f_bitrate = ""
        f_start_time = ""
        f_resolution = ""
        f_fps = ""
        f_crf = ""
        f_codec = ""
        f_progress = ""
        if bitrate:
            f_bitrate = f"""-b:v {bitrate}"""
        if start_time:
            f_start_time = f"""-ss {start_time} """
        if scale:
            # f_resolution = f"-vf scale={scale}:-2 "
            f_resolution = f"-vf scale={scale[0]}:{scale[1]} "
        if fps:
            f_fps = f"""-r {fps} """
        if crf:
            f_crf = f"""-crf {crf} """
        if progress:
            f_progress = f"""-progress progress.log"""
        if codec:
            # f_codec = "-c:v libx264"
            f_codec = f"-c:v {codec}"
        cmd = f"""{ffmpeg} -i {INPUT_VIDEO} {f_start_time}{f_resolution}{f_fps}{f_codec} {f_crf}{f_progress} {f_bitrate} {OUTPUT_FILE}  -loglevel quiet"""
        subprocess.call(cmd, shell=True)
        return OUTPUT_FILE

    # 切割一段时间视频
    def clip_video_start_end(self, INPUT_VIDEO, OUTPUT_FILE, start_time=90, end_time=-90, ffmpeg=None):
        self.remove_file(OUTPUT_FILE)
        if not ffmpeg:
            ffmpeg = self.ffmpeg
        cmd = f"""{ffmpeg} -i {INPUT_VIDEO} -ss {start_time} -to {end_time} {OUTPUT_FILE}"""
        subprocess.call(cmd, shell=True)
        return OUTPUT_FILE

    # 等间距切割视频
    def clip_video2(self, INPUT_VIDEO, segment_time=5 * 60, ffmpeg=None):
        if not ffmpeg:
            ffmpeg = self.ffmpeg
        """
        :param INPUT_VIDEO: 
        :param segment_time: 间隔
        :return: 
        -i input_video.mp4: 输入视频文件的路径和文件名。
        -c copy: 使用“copy”编解码器，将视频从输入直接复制到输出，不做任何修改。
        -map 0: 将输入文件中的所有流全部复制到输出文件中。
        -segment_time 60: 视频分段的时间长度，这里设置为60秒。
        -f segment: 指定输出格式为分段的视频格式。
        output_%03d.mp4: 输出文件的名称格式，%03d 表示输出文件名以 3 位数字为格式，例如 output_001.mp4。
        """
        output_folder = os.path.splitext(INPUT_VIDEO)[0]
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        cmd = fr"{ffmpeg} -i {INPUT_VIDEO} -c copy -map 0 -segment_time {segment_time} -f segment {output_folder}/output_%03d.mp4 -loglevel quiet"""
        subprocess.call(cmd)
        return output_folder

    # 获取视频总时长
    def get_video_duration(self, INPUT_VIDEO, ffprobe=None):
        if not ffprobe:
            ffprobe = self.ffprobe
        cmd = f"""{ffprobe}  -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {INPUT_VIDEO}"""
        total_duration = float(subprocess.check_output(cmd, shell=True))
        return total_duration

    # <editor-fold desc="获取视频总时长">
    def get_video_duration_2(self, filename):
        cap = cv2.VideoCapture(filename)
        if cap.isOpened():
            rate = cap.get(5)
            frame_num = cap.get(7)
            duration = frame_num / rate
            return duration
        return -1

    # </editor-fold>
    # 要获取视频的帧率（fps）
    def get_video_fps(self, INPUT_VIDEO, ffprobe=None):
        """

        :param INPUT_VIDEO:
        :param ffprobe:
        :return:
        要获取视频的帧率（fps），可以使用以下FFmpeg命令：

ffprobe -v error -select_streams v:0 -show_entries stream=avg_frame_rate -of default=noprint_wrappers=1:nokey=1 input.mp4
在这个命令中，-select_streams v:0 表示选择第一个视频流进行分析，-show_entries stream=avg_frame_rate 表示输出平均帧率，
-of default=noprint_wrappers=1:nokey=1 表示将结果格式化为纯数字输出。最后的参数 input.mp4 表示输入视频的路径和名称。
执行这个命令后，你将会得到一个数字，表示视频的平均帧率。如果你想要获取每一帧的帧率，可以将 avg_frame_rate 替换为 r_frame_rate。
        """
        if not ffprobe:
            ffprobe = self.ffprobe
        cmd = f"""{ffprobe} -v error -select_streams v:0 -show_entries stream=avg_frame_rate -of default=noprint_wrappers=1:nokey=1 {INPUT_VIDEO}"""
        fps = int(subprocess.check_output(cmd, shell=True).replace(b'/1\r\n', b'').decode())
        return fps

    # FFmpeg获取视频的分辨率
    def get_video_scale(self, INPUT_VIDEO, ffprobe=None):
        """
        要使用FFmpeg获取视频的分辨率，可以使用以下命令：
        ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 input.mp4
        在这个命令中，-select_streams v:0 表示选择第一个视频流进行分析，-show_entries stream=width,height
        表示输出视频的宽度和高度，-of csv=s=x:p=0 表示以宽x高的格式输出分辨率。最后的参数 input.mp4 表示输入视频的路径和名称。
        执行这个命令后，你将会得到视频的分辨率，例如 1920x1080。
        希望这个命令可以帮助你获取视频的分辨率信息。如果你有任何其他问题，请随时向我提问。
                :param INPUT_VIDEO:
        :param ffprobe:
        :return:
        """
        if not ffprobe:
            ffprobe = self.ffprobe
        cmd = f"""{ffprobe}  -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 {INPUT_VIDEO}"""
        scale = list(subprocess.check_output(cmd, shell=True).replace(b'\r\n', b'').decode().split('x'))
        return scale

    # ffmpeg获取视频码率
    def get_video_bitrate(self, INPUT_VIDEO, ffprobe=None):
        """
        在这个命令中，将"your_video_file.mp4"替换为你的视频文件名。执行该命令后，FFprobe 将输出视频文件的码率信息。
        这条命令会告诉FFprobe只选择视频流（v:0），然后显示视频流的码率信息。执行该命令后，你将会看到类似于"bit_rate=123456"的输出，其中的数字表示视频的码率。
        :param INPUT_VIDEO:
        :param ffprobe:
        :return:
        """
        if not ffprobe:
            ffprobe = self.ffprobe
        cmd = f"""{ffprobe} -v error -select_streams v:0 -show_entries stream=bit_rate -of default=noprint_wrappers=1 {INPUT_VIDEO}"""
        check_output = subprocess.check_output(cmd, shell=True)
        bitrate = int(int(check_output.split(b'=')[-1].replace(b'\r\n', b'').decode()) / 1000)  # kb/s
        return bitrate

    # ffmpeg获取视频编码
    def get_video_codec(self, INPUT_VIDEO, ffprobe=None):
        """
        要获取视频文件的编码信息，你可以使用以下命令：
        ffprobe -v error -select_streams v:0 -show_entries stream=codec_name -of default=noprint_wrappers=1 your_video_file.mp4
        在这个命令中，将"your_video_file.mp4"替换为你的视频文件名。执行该命令后，FFprobe 将输出视频文件的编码信息。
        这条命令会告诉FFprobe只选择视频流（v:0），然后显示视频流的编码信息。执行该命令后，你将会看到类似于"codec_name=h264"的输出，其中的"h264"表示视频的编码格式。
        通过这种方式，你可以方便地获取视频文件的编码信息。
        :param INPUT_VIDEO:
        :param ffprobe:
        :return:
        """
        if not ffprobe:
            ffprobe = self.ffprobe
        cmd = f"""{ffprobe} -v error -select_streams v:0 -show_entries stream=codec_name -of default=noprint_wrappers=1 {INPUT_VIDEO}"""
        check_output = subprocess.check_output(cmd, shell=True)
        codec = check_output.split(b'=')[-1].replace(b'\r\n', b'').decode()
        return codec

    # ffmpeg获取视频参数
    def get_video_params(self, INPUT_VIDEO, ffprobe=None):
        if not ffprobe:
            ffprobe = self.ffprobe
        """
           # f"stream=codec_name," \
              # f"codec_type," \
              # f"width," \
              # f"height" \
              # f",bit_rate," \
              # f"duration," \
              # f"avg_frame_rate," \
              # f"r_frame_rate," \
        """
        cmd = f"{ffprobe} -v error -select_streams v:0 -show_entries " \
              f"format -of default=noprint_wrappers=1 {INPUT_VIDEO}"
        subprocess.call(cmd, shell=True)
        # print(subprocess.check_output(cmd, shell=True))

    # 拼接**视频或音频的片段。
    def merge_vodeo(self):
        PATH_MEDIA = 'Media/'
        PATH_CLIPS = 'Clips_Video/'
        FILE_CLIPS = 'List_Video.txt'
        FILE_MERGE = PATH_MEDIA + 'Demo_new.mp4'
        """FILE_CLIPS内容如下
        file 'Clips_Video/Clip_1.mp4'
        file 'Clips_Video/Clip_2.mp4'
        file 'Clips_Video/Clip_3.mp4'
        file 'Clips_Video/Clip_4.mp4'
        """
        cmd = 'ffmpeg -f concat -i ' + PATH_MEDIA + FILE_CLIPS + ' ' + FILE_MERGE
        # Execute the (Terminal) command within Python.
        subprocess.call(cmd, shell=True)


if __name__ == '__main__':
    video_obj = VideoOperation()
    file_path = "G:\电影\亮剑\output_000-0.mp4"
    video_obj.video_to_image(file_path)
    # video_obj.mp4_to_mp3(file_path, "output_000-0.mp3")

    # file_path = r"G:\图片\录屏\20231215_214306.mp4"
    # total_duration = VideoOperation().get_video_duration(file_path, )
    # print(total_duration)
    # path2 = VideoOperation().clip_video_start_end(file_path, r'G:\图片\录屏\20231215_214306-1.mp4',
    #                                               start_time=0, end_time=int(total_duration - 3))

    # sta = time.time()
    # # 视频时常
    # file_path = 'G:\电影\亮剑.mp4'
    # total_duration = VideoOperation().get_video_duration(file_path, )
    # print(1, total_duration / 60, time.time() - sta)
    # fps = VideoOperation().get_video_fps(file_path, )
    # print(2, fps, time.time() - sta)
    # scale = VideoOperation().get_video_scale(file_path, )
    # print(3, scale, time.time() - sta)
    # bitrate = VideoOperation().get_video_bitrate(file_path, )
    # print(4, bitrate, time.time() - sta)
    # codec = VideoOperation().get_video_codec(file_path, )
    # print(5, codec, time.time() - sta)
    # VideoOperation().get_video_params(file_path, )
    # # 压缩视频
    # # path1 = VideoOperation().compress_video('G:\电影\亮剑.mp4', 'G:\电影\亮剑1-2.mp4', codec=codec, scale=[1280, 720])
    # # print(1, time.time() - sta)
    # # path2 = VideoOperation().clip_video_start_end('G:\电影\亮剑1-2.mp4', 'G:\电影\亮剑1-1-1.mp4',
    # #                                               start_time=15, end_time=int(total_duration - 10))
    # # print(2, path2, time.time() - sta)
    # output_folder = VideoOperation().clip_video2(file_path)
    # for index, value in enumerate(os.listdir(output_folder)):
    #     file = os.path.join(output_folder, value)
    #     ys = os.path.join(output_folder, value.split('.')[0] + f'-{index}' + '.mp4')
    #     codec = VideoOperation().get_video_codec(file, )
    #     VideoOperation().compress_video(file, ys, codec=codec, scale=[1280, 720])
    #     os.remove(file)
