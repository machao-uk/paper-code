# LOL 图项目交接 memo：生成流程、已完成状态、审美规则与新窗口续作说明

日期：2026-06-01
项目目录：`01_WORKBENCH/LOL_IMAGE_PROJECT/`
适用场景：当前对话窗口已经过长，后续建议在新窗口继续。新窗口应优先读取本 memo，再读取旧 memo `02_PROJECT_EXPANSION_RELATIONSHIP_WALLPAPER_MEMO_2026-06-01.md`，并参考 ASHE / KAI_SA 已完成图包作为风格基准。

---

## 0. 最重要的执行原则

本项目不是随机出图，而是按“预览确认 -> 高清正式图 -> 标准文件名 -> ZIP 交付”的流水线执行。

用户的关键口令含义已经固定：

1. 用户说“预览图”
   - 只出 1 张十宫格 / 总览图。
   - 目的是快速看方向，不要直接出 10 张高清单图。
   - 总览图可以有编号和文件名文字，方便选方向。

2. 用户说“定稿”
   - 表示当前预览方向通过。
   - 不要再改风格，不要再出新版本预览。
   - 应进入正式高清单图阶段。

3. 用户说“出高清图”
   - 生成正式高清单图。
   - 如果用户指定 01-05，就先生成 01-05。
   - 如果用户指定 02-10，就生成 02-10。
   - 生成前必须先用文字确认“现在将生成哪些编号、每张是什么内容”，等用户确认后再调用图片生成。

4. 用户说“出 ZIP”或“定，出 ZIP”
   - 意思是：已经定稿，应该把已生成的正式高清图按标准文件名整理成 ZIP，并给可点击下载链接。
   - 不要把预览图打成 ZIP 冒充正式高清 ZIP。
   - 不要重新生成图，除非正式高清图还没有生成；如果还没生成，必须先说明缺哪几张，再问是否生成。

5. 用户说“停止 / 停 / 停止生成图”
   - 立刻停止所有工具调用。
   - 只用文字回复“已停止”。
   - 不要再调用 image tool、Python、GitHub、文件工具或任何其它工具。

6. 用户要求“先和我确认，不要直接开始作图”
   - 必须只用文字确认计划，不得调用图片生成工具。

---

## 1. 项目审美基线

总目标：LOL 高完成度唯美主题图宇宙计划。

总风格：
- 高级
- 唯美
- 封面级
- 8K 质感
- 细节拉满
- 抖音吸粉封面
- 手机壁纸 / 电脑壁纸 / 无文字海报 / 设定集图
- 每个英雄有独立色系和独立氛围

最高优先级参考：
1. ASHE 第一批：冰蓝银白、高级女皇感、干净壁纸、设定集结构。
2. KAI_SA 第一批：1 张 luxury design sheet + 多张纯海报 / 壁纸，多色系多主题。

用户喜欢的视觉关键词：
- 高级香水广告质感
- 奇幻电影海报感
- 女性魅力明显
- 长腿、腰线、肩颈、锁骨、礼服剪裁
- 贵气、冷艳、御姐、女王感
- 干净构图，封面级完成度
- 不要廉价网游感
- 不要杂乱 UI
- 不要大量文字
- 不要设定板混进普通海报

尺度要求：
- 可以性感、暧昧、吸粉、有身材曲线。
- 但必须高级、克制、成年化、时尚大片感。
- 禁止露点、明确性行为、色情画面。
- 生成提示词应使用“high-fashion, elegant, cinematic, covered outfit, no nudity, no explicit sexual content, graceful curves, perfume ad quality”等表达，避免粗暴触发拦截。

---

## 2. 单英雄标准模板

每位英雄默认一套 10 张，标准文件名如下：

1. `01_luxury_design_sheet.png`
2. `02_signature_poster.png`
3. `03_moonlit_chinese_fantasy.png`
4. `04_tidal_dragon.png`
5. `05_star_guardian.png`
6. `06_mobile_wallpaper.png`
7. `07_desktop_wallpaper.png`
8. `08_crystal_rose.png`
9. `09_moonlit_pure_poster.png`
10. `10_star_shrine_poster.png`

重要：
- 第 1 张必须是 luxury design sheet / 设定集豪华版。
- 设定集可以有标题、信息板、武器拆解、技能图标、配色栏、正侧背转身图、细节分解、局部特写。
- 02-10 必须是干净海报 / 壁纸，尽量无文字、无 UI、无信息面板、无设定板。
- 02-10 若生成时出现乱字、编号、水印、UI 框，视为不合格。

01_luxury_design_sheet 结构标准：
- 中央大主视觉，全身或接近全身。
- 身材比例必须漂亮：长腿、细腰、肩颈、锁骨、礼服 / 战斗服剪裁。
- 右侧或底部：武器拆解、技能元素、材质细节、配色、转身图。
- 参考 ASHE / KAI_SA 设定集，而不是普通封面上贴文字。

02-10 纯图标准：
- no text, no UI, no information panel, no design board, no watermark。
- 每张要有不同角度、不同表情、不同姿态、不同背景，避免 10 张都一个表情一个角度。
- 必须保留角色识别点：武器、发型、代表轮廓、技能元素、阵营美学。

---

## 3. 官方皮肤与服装规则

后续单人角色要优先使用官方皮肤 / 官方服装方向。

允许来源：
- 端游 League of Legends 官方皮肤
- 手游 Wild Rift 官方皮肤

选择原则：
- 优先选唯美、高级、适合壁纸和抖音封面的皮肤。
- 可以从官方皮肤中混合提炼审美，但不要完全失去英雄识别度。
- 不要把角色做成陌生原创人物。

示例：
- Jinx：Star Guardian / 星之守护者方向效果好。
- Miss Fortune：成熟女性魅力、女船长、星守、晶玫、女王感路线效果好。
- Vayne：暗夜贵族猎手 + 2-3 张浅色柔美方向。
- Caitlyn：高定女警、皮城贵族狙击手、蓝金紫、晶玫、月光贵族。
- Xayah：暮羽女王、紫红金羽翼、羽刃、冷艳羽饰礼服。
- Zeri：霓虹电光少女、祖安电能、街头动感、青绿电弧。
- Samira：沙漠玫瑰女枪手、红黑金、双枪弯刀、危险女王。
- Sivir：恕瑞玛太阳女猎手、沙漠女王、金色圆刃、太阳神庙。

---

## 4. 已完成 / 进行中状态

### 已在项目早期完成

1. ASHE / 艾希
   - 已完成第一批 10 张。
   - 作为最高优先级参考。

2. KAI_SA / 卡莎
   - 已完成第一批 10 张。
   - 作为第二优先级参考。

### 本轮对话中已完成或基本完成

3. XAYAH × RAKAN / 霞 × 洛 夫妻图
   - 第一组夫妻壁纸已生成过 10 张，用户喜欢第一组。
   - 风格：紫红金、暮羽恋人、羽翼、月光、高级香水广告、亲密但克制。
   - 用户后来要求以后关系图 / 单英雄组里可以带一张信息封面 / 设定集式封面。
   - 是否已经正式打包归档：需要新窗口复核本地文件或重新打包。

4. JINX / 金克丝
   - 方向：Star Guardian Jinx / 星之守护者。
   - 用户重点反馈：封面要竖版，身材比例要更好；details 里要有胸前礼服 / 上半身特写、武器拆解、技能信息、设定板布局。
   - 已生成并打包：`JINX_STAR_GUARDIAN_FINAL_2026-06-01.zip`。
   - 文件名规则已按 01-10 标准整理。

5. MISS_FORTUNE / 厄运小姐
   - 方向：成熟女性魅力、女船长、女王感、红黑金、星守、晶玫、月夜海盗。
   - 用户评价：这个幸运小姐做得不错。
   - 已生成并打包：`MISS_FORTUNE_FINAL_2026-06-01.zip`。

6. VAYNE / 薇恩
   - 方向：暗夜贵族猎手，黑紫银，弩，吸血鬼猎人，冷艳长腿腰线。
   - 用户要求加入 2-3 张浅色柔美方向。
   - 曾生成两组，每组 10 张，共 20 张，用户要求“这俩打包成一个 ZIP”。
   - 已打包：`VAYNE_TWO_BATCHES_FINAL_8K_2026-06-01.zip`。
   - 另有一个早期 `VAYNE_FINAL_8K_2026-06-01.zip`，但最终更推荐 20 张合包。

7. CAITLYN / 凯特琳
   - 用户对前几版不满意，要求“性感女警别做丑”。
   - 最终采用两版融合：高定皮城女警、蓝金紫、狙击枪、贵族女警、晶玫、星坛。
   - 已生成 10 张高清并打包：`CAITLYN_FINAL_8K_2026-06-01.zip`。

8. XAYAH / 霞 单人
   - 方向：暮羽女王、紫红金、羽刃、月光、冷艳羽饰礼服。
   - 用户指出 01 design sheet 最初漏了，后面补做。
   - 01 文件：`xayah_01_luxury_design_sheet.png`。
   - 已打包：`XAYAH_FINAL_8K_2026-06-01.zip`。

9. ZERI / 泽丽
   - 方向多次试稿，用户最后定第一版。
   - 第一版：霓虹电光少女、青绿电弧、祖安街头、动感科技。
   - 已打包：`ZERI_FINAL_8K_2026-06-01.zip`。

10. SAMIRA / 莎弥拉
   - 方向：沙漠玫瑰女枪手，红黑金，双枪弯刀，成熟女王，危险性感，电影动作海报。
   - 用户定稿后已生成高清并打包：`SAMIRA_FINAL_8K_2026-06-01.zip`。

### 当前进行中：SIVIR / 希维尔

11. SIVIR / 希维尔
   - 方向：恕瑞玛太阳女猎手、沙漠女王、金色圆刃、太阳神庙、异域高级性感。
   - 用户说“这个身材应该画好一点”。
   - 第一版预览图：除了第 1 张不好，其它 02-10 都很好。
   - 用户要求第 1 张按照 Xayah 的 luxury design sheet 标准重做。
   - `sivir_01_luxury_design_sheet.png` 已重做，用户评价“完美”。
   - 当前卡点：尚未稳定完成并打包正式 `SIVIR_FINAL_8K_2026-06-01.zip`。
   - 正确下一步不是直接生成，而是先和用户确认 01-05 或 02-10 的生成计划。

Sivir 当前应该执行的清单：

1. `01_luxury_design_sheet.png`
   - 使用用户已确认完美的 `sivir_01_luxury_design_sheet.png`。

2. `02_signature_poster.png`
   - 按第一版预览中用户认可的正统封面方向。
   - 沙漠女王、圆刃、金色神庙、身材曲线更好。
   - 无文字、无 UI、无信息面板。

3. `03_moonlit_chinese_fantasy.png`
   - 月光 / 东方幻想 / 金白纱裙 / 沙漠神女。
   - 无文字。

4. `04_tidal_dragon.png`
   - 水龙与圆刃战斗海报。
   - 蓝金色调，动感强。
   - 无文字。

5. `05_star_guardian.png`
   - 星光守护者风，浅色、梦幻、适合吸粉。
   - 无文字。

6. `06_mobile_wallpaper.png`
   - 竖屏手机壁纸，人物居中，长腿腰线明显。
   - 干净无文字。

7. `07_desktop_wallpaper.png`
   - 横屏电脑壁纸，沙漠神庙大场景，人物和圆刃识别度强。
   - 无文字。

8. `08_crystal_rose.png`
   - 晶玫 / 白金玫瑰 / 柔美礼服风。
   - 高级漂亮路线，无文字。

9. `09_moonlit_pure_poster.png`
   - 无文字月光纯海报，干净、氛围感强。

10. `10_star_shrine_poster.png`
   - 终版星坛 / 太阳神殿 / 女王王座感。
   - 压轴图，无文字。

建议新窗口继续时，先对用户说：
“我先确认：现在生成 Sivir 的 01-05。01 用已定稿的 design sheet；02-05 分别是 signature poster、moonlit chinese fantasy、tidal dragon、star guardian。02-05 全部无文字无 UI。你确认我再开始。”

如果用户确认，再生成 01-05 或 02-05。不要未确认就调用图片生成。

---

## 5. 后续英雄计划

女 ADC 阶段目前基本进度：

已完成 / 已打包：
- ASHE
- KAI_SA
- JINX
- MISS_FORTUNE
- VAYNE
- CAITLYN
- XAYAH
- ZERI
- SAMIRA

进行中：
- SIVIR：01 已定稿；02-10 需正式高清并打包。

待做：
- KALISTA

Kalista 推荐方向：
- 复仇之矛
- 暗影岛幽蓝绿
- 亡灵女王 / 灵魂誓约 / 幽魂战矛
- 冷艳、危险、半透明魂火、破碎王冠、长矛、战场亡魂
- 不能做成廉价鬼图，要做成高级暗黑女神、幽冥战姬、电影海报感。

女 ADC 完成后，按旧 memo 进入：男性 ADC 或全位置循环。

---

## 6. 新窗口推荐工作流

### A. 开局读取顺序

新窗口开始时，让模型读取：

1. `01_WORKBENCH/LOL_IMAGE_PROJECT/03_SESSION_HANDOFF_MEMO_IMAGE_GENERATION_RULES_AND_STATUS_2026-06-01.md`
2. `01_WORKBENCH/LOL_IMAGE_PROJECT/02_PROJECT_EXPANSION_RELATIONSHIP_WALLPAPER_MEMO_2026-06-01.md`
3. 若需要风格参考，再读取用户上传的 ASHE / KAI_SA ZIP 图包。

### B. 预览阶段

用户要求预览时：
- 只生成一张 10 格总览图。
- 总览图可带编号和标题。
- 不打包。
- 不生成 10 张单图。

### C. 定稿阶段

用户说“定稿”时：
- 先用文字确认即将生成哪些编号。
- 如果用户说“一次输出五张”，就只生成 5 张。
- 生成前必须确认，不要擅自启动。

### D. 高清阶段

高清图要求：
- 8K质感、高清、精修、封面级。
- 除 01 design sheet 外，其余图必须无文字、无 UI、无设定板。
- 每张要不同姿态、角度、表情、场景。
- 不能把预览小格直接裁切放大；应该按预览方向重新生成对应单图。

### E. 打包阶段

打包 ZIP 前必须确保：
- 01-10 都是正式高清单图。
- 文件名是标准英文名。
- ZIP 内有 `MANIFEST.md`。
- 最终回复必须给 markdown 格式 sandbox 链接，例如：
  `[下载 SIVIR_FINAL_8K_2026-06-01.zip](sandbox:/mnt/data/SIVIR_FINAL_8K_2026-06-01.zip)`

不要只输出 `/mnt/data/...zip` 本地路径；那不是可点击下载链接。

---

## 7. 生成提示词模板

### 7.1 通用高清单图模板

Use this as the underlying direction when generating a formal image:

`A high-end cinematic fantasy poster of [CHAMPION], official League of Legends inspired skin direction [SKIN/THEME], 8K quality, ultra detailed, premium perfume advertisement quality, elegant mature beauty, graceful body proportions, long legs, defined waistline, refined shoulders and neckline, covered high-fashion battle outfit, iconic weapon clearly visible, clean composition, no text, no UI, no watermark, no info panel, no design board, cinematic lighting, luxury materials, sharp face, strong character identity, not cheap game ad, not cluttered, no nudity, no explicit sexual content.`

### 7.2 01 luxury design sheet 模板

`A vertical luxury character design sheet for [CHAMPION], official League of Legends inspired [SKIN/THEME], premium game art concept sheet, central full-body hero artwork, elegant mature proportions, iconic weapon breakdown, ability VFX details, outfit material close-ups, color palette, turnaround mini poses, refined information board layout, high-end ASHE/KAI'SA design sheet reference, clean professional layout, 8K quality, fantasy cinematic lighting, beautiful but respectful, no nudity, no explicit sexual content.`

### 7.3 02-10 禁止项

For 02-10 always add:

`no text, no lettering, no captions, no UI, no panels, no character sheet, no design board, no watermark, clean poster only.`

---

## 8. 用户偏好和踩坑记录

用户强烈不喜欢：
- 卡住不回复。
- 说“定稿”后又出预览或改风格。
- 说“出 ZIP”后只给本地路径 `/mnt/data/...`，不是可点击链接。
- 把预览图 ZIP 当高清正式 ZIP。
- 生成前没有确认清楚。
- 用户喊停后还继续调用工具。
- 十张图同角度同表情。
- 图片里出现乱七八糟的文字。
- design sheet 不像 ASHE / KAI_SA 的设定集，而像普通海报。
- Caitlyn 被画丑、Zeri 静态站桩、Sivir 身材不够好。

用户喜欢：
- 第一组 Xayah × Rakan 的高级紫红金情侣感。
- Jinx 星守封面的身材比例和 details 方向。
- Miss Fortune 成熟吸粉风格。
- Vayne 暗夜 + 柔美浅色混合方向。
- Caitlyn 两版融合后的高定女警。
- Xayah 的 01 luxury design sheet 补做方向。
- Zeri 第一版。
- Samira 第一版。
- Sivir 除第一张外的第一版总览，以及后来补做的 01 luxury design sheet。

关键提醒：
- 用户语气急时，优先停止和确认，不要辩解。
- 不要输出空图片工具调用。
- 不要生成用户没有明确授权的下一步。
- 如果要分批，必须先文字确认批次编号。

---

## 9. 新窗口继续时的首句建议

如果新窗口要继续 Sivir，推荐先回复：

“我已读取交接 memo。当前 Sivir 状态：01_luxury_design_sheet 已定稿；02-10 需要按第一版预览方向生成正式高清单图。现在我先确认：本轮只生成 01-05，01 使用已定稿 design sheet，02-05 分别是 signature poster、moonlit chinese fantasy、tidal dragon、star guardian；02-05 全部无文字、无 UI、无设定板。你确认后我再开始生成。”

不要在这句之前调用图片生成。
