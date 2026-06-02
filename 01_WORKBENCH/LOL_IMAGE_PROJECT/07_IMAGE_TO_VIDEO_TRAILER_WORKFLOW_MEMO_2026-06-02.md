# LOL_IMAGE_PROJECT 续作 memo：图生视频 / 10 秒终极皮肤预告片工作流

日期：2026-06-02  
项目目录：`01_WORKBENCH/LOL_IMAGE_PROJECT/`  
用途：记录当前发现的图生视频新工作流：使用 Gemini / Veo 的 image-to-video 功能，把已定稿静态角色图转换成 8-10 秒动态预告片，用于抖音停留、吸粉和“老玩家青春重铸计划”的视频化升级。

---

## 0. 重大更新：项目从“图包”升级到“预告片”

当前项目原本是：

1. 生成十宫格预览图。
2. 用户审核方向。
3. 生成正式高清 01-10 单图。
4. 打包 ZIP。
5. 发抖音 / 做收藏图。

现在新增一层：

**每个主角 / 每个重点系列都可以额外做 1 条 8-10 秒图生视频预告片。**

这意味着项目不再只是“终极皮肤设定集”，而是可以升级为：

**老玩家青春重铸预告片。**

账号内容形态升级为：

- 静态图：终极皮肤设定集 / 高清海报 / 壁纸。
- 动态视频：终极皮肤预告片 / 情绪短片 / 角色登场镜头。

---

## 1. 已验证样例：Sivir 金色神殿图生视频

测试图：Sivir / 希维尔金色神殿主海报。  
测试工具：Gemini Pro 内置的视频 / Veo 图生视频功能。  
测试结果：可以生成约 10 秒 MP4 视频。

观察到的有效点：

- 镜头推进可以成立。
- 角色整体能保持基本稳定。
- 头发、纱裙、金色粒子、光效、环境氛围可以动。
- 能做出“终极皮肤预告片”的感觉。
- 对抖音短视频来说已经够用。

观察到的风险：

- 工具不是简单局部动图，而是会对原图进行一定程度的视频化重构。
- 背景、站位、局部构图可能变化。
- 如果 prompt 不够严格，可能改脸、改衣服、改武器、改姿态。
- 不能让角色做复杂动作，否则容易崩。

结论：

**这条路线可用。每个主角都可以挑 1 张最强正式图，做 8-10 秒图生视频预告片。**

---

## 2. 图生视频不是传统 CG，但足够用于抖音

必须明确：

这不是传统 3D CG，不是完整角色动画工作室流程。

它更适合生成：

- 8-10 秒单镜头角色登场。
- 镜头缓慢推进。
- 头发、衣袖、纱裙、尾巴、粒子、光效、烟雾、蛛丝、红线、雾气轻微运动。
- 角色轻微呼吸、眼神变化、回眸、抬头、凝视。
- 环境灯光变化、能量闪烁。

不适合生成：

- 长时间剧情动画。
- 多镜头连续叙事。
- 精确打斗动作。
- 多角色复杂交互。
- 角色大幅转身、奔跑、跳舞、连招。
- 严格保持每一帧完全一致的专业 CG。

因此项目策略是：

**少动角色，多动环境。**

最稳的动作元素：

- 镜头推进 / dolly in
- 头发轻动
- 丝带 / 纱裙 / 衣袖轻动
- 粒子飘动
- 魔法光效闪烁
- 烟雾 / 雾气流动
- 背景灯笼 / 神殿光影轻微变化
- 角色眼神轻微变化

---

## 3. 标准视频工作流

每个角色 / 系列建议形成“三件套”：

### A. 十宫格预览图

用途：方向审核。  
特点：一张图内展示 10 个方向，可以有编号和标题。  
不用于最终 ZIP 冒充正式图。

### B. 正式高清 01-10 单图

用途：收藏图、壁纸、图包、抖音图集。  
特点：01 是 luxury design sheet，02-10 是干净海报 / 壁纸。  
要求：02-10 无文字、无 UI、无设定板、无水印。

### C. 8-10 秒图生视频预告片

用途：抖音停留、吸粉、动态预告、爆款测试。  
做法：从 01-10 中选择最强的一张，上传到 Gemini / Veo，使用视频 prompt 做图生视频。

推荐优先选图：

1. `02_signature_poster.png`
2. `10_finale / 10_xxx_finale.png`
3. 情绪强的 `09_portrait` 或 `08_farewell_portrait`
4. Sona × Seraphine 这类关系图可优先选 `09_soft_yuri_portrait` 或 `02_moonlight_duet_poster`

---

## 4. 通用图生视频 prompt 模板

上传定稿图后，使用如下结构：

```text
Use the uploaded image as the exact visual reference. Keep the same character design, face, outfit, weapon, colors, lighting, background, body proportions, and original composition.

Create an 8-10 second cinematic fantasy game trailer shot.

Scene:
[描述角色站在哪里，环境是什么，哪些元素轻微动起来。]

Camera:
Slow cinematic push-in from [full-body / medium shot] to [closer portrait / waist-up shot]. Smooth motion, no sudden cuts.

Motion:
Only animate subtle environmental and atmospheric elements: hair, fabric, ribbons, particles, magical light, smoke, mist, petals, fire, water, foxfire, spider silk, red threads. Keep the character pose mostly stable.

Mood:
[高级、唯美、暗黑、温柔、悲剧、史诗等。]

Audio:
[风声、魔法光效、神殿环境音、钟声、琴声等。No speech unless specifically needed.]

Avoid:
No text, no subtitles, no logo, no watermark, no extra characters, no changing the face, no changing the outfit, no changing the weapon, no changing the body proportions, no distorted hands, no fast action, no fighting unless explicitly requested, no low-quality animation, no vulgarity.
```

核心硬句：

```text
Keep the original composition. Do not redesign the scene. Do not change the outfit, face, weapon, pose, or body proportions. Only animate hair, fabric, particles, light, mist, and camera movement.
```

---

## 5. Sivir 已验证 prompt 记录

测试使用的 Sivir prompt：

```text
Use the uploaded image as the exact visual reference. Keep the same character design, face, outfit, golden circular blade, desert temple, lighting, colors, and composition.

Create an 8-second cinematic fantasy game trailer shot.

Scene:
A desert queen warrior stands in a golden ancient temple. Warm sunlight shines through the ruins. Her long hair and translucent silk ribbons move gently in the wind. Golden dust particles float in the air. The circular blade glows softly with solar energy. Small sparks and sand motes drift around her.

Camera:
Slow cinematic push-in from a full-body hero shot to a closer waist-up portrait. Smooth motion, no sudden cuts.

Mood:
Epic, elegant, high-end fantasy game trailer, ultimate skin reveal, golden desert goddess atmosphere.

Audio:
Soft desert wind, faint golden magic shimmer, distant temple ambience. No speech.

Avoid:
No text, no subtitles, no logo, no watermark, no extra characters, no changing the face, no changing the outfit, no changing the weapon, no distorted hands, no fast action, no fighting, no vulgarity.
```

该 prompt 成功验证：

- 10 秒视频可用。
- 镜头推进有效。
- 金色粒子、头发、纱裙、光效适合运动。
- 适合做“终极皮肤预告片”。

---

## 6. Ahri / 阿狸图生视频策略

Ahri 非常适合图生视频。

最适合运动元素：

- 九尾缓慢摆动
- 狐火球漂浮
- 花瓣飘动
- 神社灯笼微闪
- 丝带和长发轻动
- 月光增强
- 镜头从全身推到近景

Ahri 视频 prompt：

```text
Use the uploaded image as the exact visual reference. Keep the same character design, face, outfit, fox ears, nine tails, foxfire orbs, colors, lighting, and original composition.

Create an 8-10 second cinematic fantasy game trailer shot.

Scene:
A nine-tailed fox goddess stands in a moonlit shrine. Her nine tails gently sway in the night breeze. Small foxfire orbs float around her. Silk ribbons and long hair move softly. Petals drift through the air. The moonlight glows behind her and shrine lanterns flicker gently.

Camera:
Slow cinematic push-in from a medium full-body shot to a closer portrait shot. Smooth motion, no sudden cuts.

Mood:
Elegant, magical, premium fantasy game trailer, high-end ultimate skin reveal, moon fox goddess atmosphere, beautiful and mysterious.

Audio:
Soft magical wind, gentle foxfire shimmer, faint shrine bell sound. No speech.

Avoid:
No text, no subtitles, no logo, no watermark, no extra characters, no changing the face, no changing the outfit, no changing the hairstyle, no changing the nine tails, no distorted hands, no fighting, no fast movement, no vulgarity.
```

Ahri 抖音视频标题建议：

- 阿狸终极皮肤如果真的上线，预告片可能长这样。
- 评论区点名最多的阿狸，我让她动起来了。
- 九尾妖狐终极皮肤预告片，老玩家顶得住吗？

---

## 7. 四妹 / 盘丝岭意难平图生视频策略

四妹非常适合图生视频，尤其适合情绪短片。

最适合运动元素：

- 蛛丝轻轻晃动
- 红线飘起
- 山雾流动
- 灯笼微微闪烁
- 头发和衣袖轻动
- 她轻微回眸 / 眼神转向镜头
- 镜头穿过蛛丝缓慢推进

四妹视频 prompt：

```text
Use the uploaded image as the exact visual reference. Keep the same character design, face, hairstyle, outfit, colors, spider silk, red thread, moonlight, Pansi Ridge atmosphere, and original composition.

Create an 8-10 second cinematic Chinese dark fantasy trailer shot.

Scene:
The Fourth Sister stands inside a moonlit spider cave. Hanging spider silk moves gently. Red threads drift in the air. Old lanterns flicker softly. Pale mist flows across the ground. Her hair and sleeves move slightly in the night wind. She slowly turns her eyes toward the camera with a sad, unforgettable expression.

Camera:
Slow forward dolly through hanging silk threads, ending in a close emotional portrait. Smooth, quiet, no cuts.

Mood:
Tragic, beautiful, mysterious, gentle but dangerous, unforgettable regret, cinematic Chinese fantasy, the feeling of meeting, saving, and missing someone forever.

Audio:
Soft wind through the cave, faint silk movement, distant bell or lantern sound. No speech.

Avoid:
No text, no subtitles, no logo, no watermark, no extra characters, no modern objects, no gore, no jump scare, no exaggerated movement, no changing the character design, no changing the face, no vulgarity.
```

四妹抖音视频标题建议：

- 黑神话里最意难平的女人，我让她动起来了。
- 四妹如果有终极电影预告片，会不会就是这样？
- 见过，救过，错过。盘丝岭这一眼真的忘不了。

---

## 8. Sona × Seraphine 图生视频策略

Sona × Seraphine 的视频不应做大动作，而应做“似有似无”的亲密氛围。

最适合运动元素：

- 舞台灯光柔和变化
- 发丝轻动
- 琴弦发光
- 麦克风水晶闪烁
- 手指差一点碰到
- 两人轻微靠近
- 镜头慢推到双人近景

视频 prompt 基调：

```text
Use the uploaded image as the exact visual reference. Keep the same character designs, faces, outfits, instruments, colors, lighting, and original composition.

Create an 8-10 second cinematic romantic music trailer shot.

Scene:
Sona and Seraphine share a quiet moonlit stage after a performance. Soft blue-violet and pink-violet lights glow around them. Sona's Etwahl strings shimmer gently. Seraphine's crystal microphone glows softly. Their hair and ribbons move slightly. Their hands move closer near the glowing music, almost touching but not touching.

Camera:
Slow cinematic push-in from a two-person medium shot to a close emotional portrait. Smooth motion, no cuts.

Mood:
Tender, elegant, dreamy, soft romantic tension, healing duet, beautiful female intimacy, pure but not explicit.

Audio:
Soft piano-like notes, faint string shimmer, gentle stage ambience. No speech.

Avoid:
No text, no subtitles, no logo, no watermark, no extra characters, no changing faces, no changing outfits, no vulgarity, no explicit content, no exaggerated kissing, no fast movement.
```

---

## 9. Kalista 图生视频策略

Kalista 的图生视频应走暗影岛亡灵预告片。

最适合运动元素：

- 黑雾流动
- 魂火燃起
- 长矛幽光
- 破碎王冠光影
- 亡灵剪影轻动
- 镜头低机位推进

Kalista prompt 基调：

```text
Use the uploaded image as the exact visual reference. Keep the same character design, face, ghostly armor, long spear, teal soulfire, Shadow Isles mist, colors, and original composition.

Create an 8-10 second dark fantasy game trailer shot.

Scene:
Kalista stands in the black mist of the Shadow Isles. Teal soulfire burns around her spear. Ghostly fog moves across the ruined battlefield. Her spectral hair and tattered cloth move slightly. Faint oathbound spirits appear and fade behind her.

Camera:
Slow low-angle push-in from full-body silhouette to a cold close portrait. Smooth motion, no sudden cuts.

Mood:
Tragic, cold, dangerous, undead vengeance goddess, premium dark fantasy game trailer.

Audio:
Low ghostly wind, faint spectral flame, distant whisper-like ambience. No speech.

Avoid:
No text, no subtitles, no logo, no watermark, no extra characters, no redesigning the character, no cute animation style, no cheerful colors, no gore, no vulgarity.
```

---

## 10. 发布策略

以后每个重点角色可以发两条或三条：

### 方案 1：两条法

1. 十宫格预览 / 设定集图：展示完整方向。
2. 10 秒图生视频：展示最强主视觉动起来。

### 方案 2：三条法

1. 十宫格预览图：评论区审核 / 点名。
2. 正式高清 01-10 图集：收藏向。
3. 10 秒图生视频：预告片向 / 提高停留。

推荐标题结构：

- 如果 XX 有终极皮肤，预告片可能长这样。
- 我把 XX 的终极皮肤设定集做成了预告片。
- 评论区点名的 XX，我让她动起来了。
- 老玩家青春重铸计划：XX 终极预告片。
- 这不是官方，但我真希望它是真的。

---

## 11. 当前最高优先级视频对象

### 第一优先级：Ahri

原因：评论区大量点名，男女用户都想看。  
视频卖点：九尾摆动、狐火漂浮、神社灯笼、月光花瓣。

### 第二优先级：四妹

原因：国产游戏情绪核弹，意难平非常适合短视频。  
视频卖点：蛛丝、红线、回眸、山雾、灯笼、遗憾感。

### 第三优先级：Sona × Seraphine

原因：双人吸粉系列，适合做温柔暧昧短片。  
视频卖点：手指差一点碰到、琴弦发光、舞台柔光、双人近景。

### 第四优先级：Kalista

原因：女性射手阶段暗黑收尾。  
视频卖点：魂火、长矛、黑雾、亡灵女神压迫感。

---

## 12. 硬规则

1. 不要直接让视频模型从零生成角色，优先上传我们已经定稿的高清图。
2. 一次只要求一个明确镜头，不要贪多。
3. 不要让角色做复杂动作，优先动环境、光效、头发、布料和粒子。
4. 每条视频尽量控制在 8-10 秒。
5. 不要出现文字、字幕、logo、水印、额外人物。
6. 不要让模型改变脸、服装、武器、体型和构图。
7. 如果视频工具重构过度，换更保守 prompt：只允许 camera push-in + particles + fabric + light。
8. 图生视频用于抖音动态内容，不替代正式高清图包。
9. 继续保留原本工作流：预览确认 -> 高清单图 -> ZIP -> 视频预告片。
