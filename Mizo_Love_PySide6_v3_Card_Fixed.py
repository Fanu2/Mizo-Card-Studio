import sys, random
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtGui import QFont, QPixmap, QPainter, QLinearGradient, QBrush, QPen
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton, QListWidget,
    QListWidgetItem, QLineEdit, QComboBox, QTextEdit, QVBoxLayout, QHBoxLayout,
    QFrame, QMessageBox
)

# Larger v2 content set.
# "Reference" entries are based on published Mizo phrase resources.
# "Practice" entries are learning-oriented templates and should be checked
# with a fluent Mizo speaker before sending as a polished romantic message.

DATA = [
# category, English, Mizo, note, source label
("❤️ Core Love","I love you","Ka hmangaih che","Core romantic declaration.","Reference"),
("❤️ Core Love","Do you love me?","Min hmangaih em?","A direct romantic question.","Reference"),
("❤️ Core Love","Yes, I love you.","Aw, ka hmangaih che.","Direct reply.","Reference"),
("❤️ Core Love","I don't love you.","Aih, ka hmangaih lo che.","Negative form listed in a Mizo phrase resource.","Reference"),
("❤️ Core Love","I miss you.","Ka ngai che.","Simple expression of longing.","Reference"),
("❤️ Core Love","I miss you too.","Keipawhin ka ngai che.","Reply expressing mutual longing.","Reference"),
("❤️ Core Love","I don't miss you.","Ka ngai lo che.","Negative form.","Reference"),
("❤️ Core Love","I like you.","Ka duh che.","Romantic/affectionate liking.","Reference"),
("❤️ Core Love","I really like you.","Ka duh tak zet!","Strong liking.","Reference"),
("❤️ Core Love","I am in love.","Ka inhmangaih em em a.","Romantic state of being in love.","Reference"),
("❤️ Core Love","I'm yours.","I ta ka ni.","Strong romantic/devotional expression.","Reference"),
("❤️ Core Love","You're very special!","I special hle mai!","Affectionate compliment.","Reference"),
("❤️ Core Love","You look beautiful!","I hmel a mawi hle mai!","Romantic compliment.","Reference"),
("❤️ Core Love","You look gorgeous.","I mawi hle mai.","Romantic compliment.","Reference"),
("❤️ Core Love","You have a beautiful name.","Hming mawi tak i nei a","Compliment about someone's name.","Reference"),
("❤️ Core Love","My heart speaks the language of love.","Ka thinlung hian hmangaihna tawng a hmang a","Poetic romantic expression.","Reference"),
("❤️ Core Love","Would you marry me?","Min nei dawn em ni?","Marriage proposal.","Reference"),
("❤️ Core Love","I would like to invite you to dinner.","Zanriah ei turin ka sawm duh che u a ni","Romantic/social invitation.","Reference"),
("❤️ Core Love","Are you free tomorrow evening?","Naktuk tlaiah i zalen tawh em?","Invitation opener.","Reference"),
("❤️ Core Love","Can you tell me more about you?","I chanchin min hrilh belh thei ang em?","Getting-to-know-you question.","Reference"),

("🌹 Compliments","You are beautiful.","I hmel a mawi hle mai!","Beauty compliment.","Reference"),
("🌹 Compliments","You look beautiful.","I hmel a mawi hle mai!","Appearance compliment.","Reference"),
("🌹 Compliments","You look gorgeous.","I mawi hle mai.","Appearance compliment.","Reference"),
("🌹 Compliments","You have a beautiful name.","Hming mawi tak i nei a","Name compliment.","Reference"),
("🌹 Compliments","You're very special.","I special hle mai!","Affectionate compliment.","Reference"),
("🌹 Compliments","You are funny.","A nuihzatthlak hle mai","Light-hearted compliment; wording may depend on context.","Reference"),
("🌹 Compliments","You are lovely.","Duhawm","Single-word learning item; verify sentence context.","Reference"),
("🌹 Compliments","You are lovable.","Ngainatawm","Vocabulary item meaning lovable/adorable.","Dictionary"),
("🌹 Compliments","You are beautiful to me.","I mawi hle mai","Use as a learner prompt; exact nuance may vary.","Practice"),
("🌹 Compliments","Your smile makes me happy.","—","Romantic translation exercise; enter your preferred wording and verify with a native speaker.","Practice"),
("🌹 Compliments","I love your smile.","—","Romantic translation exercise.","Practice"),
("🌹 Compliments","I love your eyes.","—","Romantic translation exercise.","Practice"),

("💌 Longing","I miss you.","Ka ngai che.","Core longing phrase.","Reference"),
("💌 Longing","I missed you.","Ka ngai che a ni","Past-tense-style expression listed by a translation resource.","Reference"),
("💌 Longing","I miss you too.","Keipawhin ka ngai che.","Mutual longing.","Reference"),
("💌 Longing","I don't miss you.","Ka ngai lo che.","Negative form.","Reference"),
("💌 Longing","I can't wait to see you again.","—","Learning prompt; verify natural Mizo wording.","Practice"),
("💌 Longing","I wish you were here.","—","Learning prompt; verify natural Mizo wording.","Practice"),
("💌 Longing","I think about you.","—","Learning prompt; verify natural Mizo wording.","Practice"),
("💌 Longing","I have been thinking about you.","—","Learning prompt; verify natural Mizo wording.","Practice"),
("💌 Longing","I want to see you.","—","Learning prompt; verify natural Mizo wording.","Practice"),
("💌 Longing","I want to talk to you.","Ka be duh che","Affectionate desire to talk.","Reference"),

("💬 Getting Closer","Hello, my friend.","Hello ka thianpa","Warm greeting.","Reference"),
("💬 Getting Closer","How are you?","I dam em?","Useful conversation opener.","Reference"),
("💬 Getting Closer","Can you tell me more about you?","I chanchin min hrilh belh thei ang em?","Getting-to-know-you question.","Reference"),
("💬 Getting Closer","Are you married?","Nupui pasal i nei tawh em?","Relationship-status question.","Reference"),
("💬 Getting Closer","I'm single.","Single ka ni","Relationship-status statement.","Reference"),
("💬 Getting Closer","I'm married.","Nupui ka nei tawh","Relationship-status statement.","Reference"),
("💬 Getting Closer","Can I have your phone number?","I phone number ka nei thei ang em?","Request for contact details.","Reference"),
("💬 Getting Closer","Do you have any pictures of you?","I thlalak i nei em?","Request for photos; use respectfully.","Reference"),
("💬 Getting Closer","Would you like to meet?","—","Learning prompt; verify natural Mizo wording.","Practice"),
("💬 Getting Closer","Can we talk?","—","Learning prompt; verify natural Mizo wording.","Practice"),
("💬 Getting Closer","Can I ask you something?","Thil ka zawt thei che angem?","Conversation opener.","Reference"),
("💬 Getting Closer","Will you come with me?","Min Kalpui Thei Ang Em?","Invitation/companionship phrase.","Reference"),
("💬 Getting Closer","I will go with you.","I rualin ka kal dawn.","Companionship phrase.","Reference"),
("💬 Getting Closer","Let's go.","Kal ang.","Simple invitation.","Reference"),

("🌙 Good Morning / Night","Good morning.","Tukchhuah nuam le","Warm morning greeting.","Reference"),
("🌙 Good Morning / Night","Good afternoon.","Chawhnulam chibai","Afternoon greeting.","Reference"),
("🌙 Good Morning / Night","Good evening.","Tlailam chibai","Evening greeting.","Reference"),
("🌙 Good Morning / Night","Good night.","Muttui","Good-night expression.","Reference"),
("🌙 Good Morning / Night","Good night, my love.","Muttui","Good-night base phrase; add a verified term of endearment separately.","Reference"),
("🌙 Good Morning / Night","Have a nice day!","Ni hman nuam le!","Warm daily wish.","Reference"),
("🌙 Good Morning / Night","See you later!","Nakinah kan inhmu dawn nia!","Warm farewell.","Reference"),
("🌙 Good Morning / Night","I will be right back!","Ka lo kir leh nghal mai ang!","Useful when briefly leaving.","Reference"),
("🌙 Good Morning / Night","Have a good trip!","Khualzinna tha tak hmang rawh!","Warm travel wish.","Reference"),
("🌙 Good Morning / Night","Sweet dreams.","—","Learning prompt; verify a natural Mizo rendering.","Practice"),

("💞 Replies","I love you.","Ka hmangaih che","Declaration.","Reference"),
("💞 Replies","Yes, I love you.","Aw, ka hmangaih che.","Affectionate reply.","Reference"),
("💞 Replies","I don't love you.","Aih, ka hmangaih lo che.","Negative reply.","Reference"),
("💞 Replies","I miss you.","Ka ngai che.","Longing reply.","Reference"),
("💞 Replies","I miss you too.","Keipawhin ka ngai che.","Mutual longing.","Reference"),
("💞 Replies","I don't miss you.","Ka ngai lo che.","Negative response.","Reference"),
("💞 Replies","I like you.","Ka duh che","Affectionate response.","Reference"),
("💞 Replies","I really like you.","Ka duh tak zet!","Stronger liking.","Reference"),
("💞 Replies","You are very special.","I special hle mai!","Affectionate affirmation.","Reference"),
("💞 Replies","I am yours.","I ta ka ni.","Devotional response.","Reference"),

("🌸 Everyday Affection","Thank you.","Ka lawm e","Useful for appreciative romantic conversation.","Reference"),
("🌸 Everyday Affection","Thank you very much.","Ka lawm lutuk e","Warm gratitude.","Reference"),
("🌸 Everyday Affection","You're welcome.","Keipawh ka lawm!","Reply to thanks.","Reference"),
("🌸 Everyday Affection","Don't worry.","Lungngai suh","Comforting phrase.","Reference"),
("🌸 Everyday Affection","I am fine, thank you.","Ka tha e, ka lawm e!","Warm conversational response.","Reference"),
("🌸 Everyday Affection","That's nice!","Chu chu a lawmawm khawp mai!","Positive reaction.","Reference"),
("🌸 Everyday Affection","Have a nice day!","Ni hman nuam le!","Kind wish.","Reference"),
("🌸 Everyday Affection","Nice to meet you.","Kan inhmu thei a lawmawm e!","Warm first-meeting phrase.","Reference"),
("🌸 Everyday Affection","Hello.","Chibai","Basic greeting.","Reference"),
("🌸 Everyday Affection","Goodbye.","Mangtha!","Farewell.","Reference"),

("💍 Serious Romance","Would you marry me?","Min nei dawn em ni?","Marriage proposal.","Reference"),
("💍 Serious Romance","Are you married?","Nupui pasal i nei tawh em?","Relationship-status question.","Reference"),
("💍 Serious Romance","I'm single.","Single ka ni","Relationship status.","Reference"),
("💍 Serious Romance","I'm married.","Nupui ka nei tawh","Relationship status.","Reference"),
("💍 Serious Romance","This is my husband.","Hei hi ka pasal a ni","Relationship/family introduction.","Reference"),
("💍 Serious Romance","This is my wife.","Hei hi ka nupui a ni","Relationship/family introduction.","Reference"),
("💍 Serious Romance","You are very special to me.","—","Learning prompt; verify natural Mizo wording.","Practice"),
("💍 Serious Romance","I want a future with you.","—","Learning prompt; verify natural Mizo wording.","Practice"),
("💍 Serious Romance","I want to stay with you.","—","Learning prompt; verify natural Mizo wording.","Practice"),
("💍 Serious Romance","I will always care about you.","—","Learning prompt; verify natural Mizo wording.","Practice"),

("🎵 Poetic / Learning","My heart speaks the language of love.","Ka thinlung hian hmangaihna tawng a hmang a","Poetic expression listed by a translation resource.","Reference"),
("🎵 Poetic / Learning","Love","Hmangaihna","Noun: love.","Dictionary"),
("🎵 Poetic / Learning","Love / to love","Hmangaih","Verb; dictionary sources give senses including love and like.","Dictionary"),
("🎵 Poetic / Learning","Lovable","Ngainatawm","Dictionary vocabulary item.","Dictionary"),
("🎵 Poetic / Learning","Lovely / beautiful","Duhawm","Dictionary vocabulary item; verify exact context.","Dictionary"),
("🎵 Poetic / Learning","My love","—","Useful English learning prompt; verify the preferred Mizo endearment with a fluent speaker.","Practice"),
("🎵 Poetic / Learning","My beloved","—","Poetic learning prompt; verify natural Mizo wording.","Practice"),
("🎵 Poetic / Learning","Beloved","—","Vocabulary/translation exercise; verify context.","Practice"),
]

SOURCES = [
("Bharatavani / CIIL", "https://bharatavani.in/mizo/dictionaries", "Government of India language resources; includes English–Mizo and Mizo learning dictionaries."),
("Bharatavani Mizo learning", "https://bharatavani.in/mizo/bhashakosha", "Mizo dictionaries, language-learning materials and literature."),
("Mizo Society of America", "https://mizousa.org/mizo-language/", "Mizo language overview, dictionaries and learning resources."),
("Languik Mizo–English", "https://languik.com/translation/mizo-to-english-translator", "Common Mizo phrases, including a dedicated romance/love section."),
("Polytranslator: I love you", "https://www.polytranslator.com/how-to-say/i-love-you/mizo/", "Reference for 'Ka hmangaih che'."),
("LearnEntry Mizo phrases", "https://www.learnentry.com/english-mizo/mizo-sentences-and-phrases/", "Common sentences and romance-related examples."),
("Kaikki Mizo dictionary", "https://kaikki.org/dictionary/Mizo/meaning/h/hm/hmangaih.html", "Dictionary entry for hmangaih: love/like."),
]

class PhraseCard(QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName("card")
        self.cat=QLabel(); self.cat.setObjectName("category")
        self.mizo=QLabel(); self.mizo.setObjectName("mizo"); self.mizo.setWordWrap(True)
        self.eng=QLabel(); self.eng.setObjectName("english"); self.eng.setWordWrap(True)
        self.note=QLabel(); self.note.setObjectName("note"); self.note.setWordWrap(True)
        self.badge=QLabel(); self.badge.setObjectName("badge")
        l=QVBoxLayout(self); l.setContentsMargins(32,28,32,28); l.setSpacing(14)
        l.addWidget(self.cat); l.addWidget(self.mizo); l.addWidget(self.eng); l.addWidget(self.badge); l.addWidget(self.note)

    def show(self,p,english=True):
        cat,en,mizo,note,src=p
        self.cat.setText(cat)
        self.mizo.setText(mizo if mizo!="—" else "Mizo wording not supplied")
        self.eng.setText(en if english else "English meaning hidden — try to recall it.")
        self.badge.setText("✓ Reference" if src=="Reference" else ("📖 Dictionary" if src=="Dictionary" else "✎ Practice / verify"))
        self.note.setText(note)

STYLE="""
QMainWindow,QWidget{background:#0f1422;color:#edf2ff;font-family:"Segoe UI";}
QLabel#title{font-size:30px;font-weight:700;color:#fff;}
QLabel#subtitle{color:#aeb9d3;font-size:13px;}
QLabel#category{color:#ff86ad;font-size:14px;font-weight:700;}
QLabel#sectionTitle{font-size:22px;font-weight:700;color:#fff;}
QLabel#cardPreview{background:#0a0f1b;border:1px solid #303b58;border-radius:12px;color:#8792ad;font-size:16px;}
QLabel#mizo{color:#ffc1d4;font-size:31px;font-weight:700;}
QLabel#english{color:#fff;font-size:22px;font-weight:600;}
QLabel#note{color:#aeb9d3;font-size:13px;}
QLabel#badge{color:#e9d7df;font-size:12px;font-weight:600;}
QFrame#card,QFrame#panel{background:#171e30;border:1px solid #2b3650;border-radius:16px;}
QLineEdit,QComboBox,QTextEdit{background:#0a0f1b;border:1px solid #303b58;border-radius:10px;padding:9px;color:#edf2ff;}
QListWidget{background:#0a0f1b;border:1px solid #2b3650;border-radius:12px;padding:6px;}
QListWidget::item{padding:10px;border-radius:8px;}
QListWidget::item:selected{background:#6d3550;}
QPushButton{background:#b83f70;border:0;border-radius:10px;padding:10px 15px;color:#fff;font-weight:600;}
QPushButton:hover{background:#d34d81;}
QPushButton#secondary{background:#2b3650;}
"""


class CardGenerator(QFrame):
    """Paste Mizo text and generate a shareable PNG card directly in the app."""
    def __init__(self):
        super().__init__()
        self.setObjectName("card")
        self.last_pixmap = None

        title = QLabel("🎨 Mizo Card Generator")
        title.setObjectName("sectionTitle")
        helptext = QLabel("Paste Mizo text below. The generated card contains Mizo only.")
        helptext.setObjectName("subtitle")

        self.text = QTextEdit()
        self.text.setPlaceholderText("Paste your Mizo expression here…")
        self.text.setFixedHeight(115)

        self.style_box = QComboBox()
        self.style_box.addItems([
            "Romantic Sunset",
            "Midnight Rose",
            "Dreamy Lavender",
            "Golden Love",
            "Ocean Heart",
            "Elegant Dark"
        ])

        self.size_box = QComboBox()
        self.size_box.addItems(["1080 × 1350  (Portrait)", "1080 × 1080  (Square)", "1920 × 1080  (Landscape)"])

        self.preview = QLabel("Your Mizo card preview will appear here")
        self.preview.setObjectName("cardPreview")
        self.preview.setAlignment(Qt.AlignCenter)
        self.preview.setMinimumHeight(300)
        self.preview.setWordWrap(True)

        buttons = QHBoxLayout()
        self.generate = QPushButton("✨ Generate Card")
        self.generate.clicked.connect(self.generate_card)
        self.save = QPushButton("💾 Save PNG")
        self.save.setObjectName("secondary")
        self.save.clicked.connect(self.save_card)
        buttons.addWidget(self.generate)
        buttons.addWidget(self.save)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(24,24,24,24)
        layout.setSpacing(12)
        layout.addWidget(title)
        layout.addWidget(helptext)
        layout.addWidget(self.text)

        opts = QHBoxLayout()
        opts.addWidget(QLabel("Design:"))
        opts.addWidget(self.style_box, 1)
        opts.addWidget(QLabel("Size:"))
        opts.addWidget(self.size_box, 1)
        layout.addLayout(opts)
        layout.addWidget(self.preview, 1)
        layout.addLayout(buttons)

    def generate_card(self):
        text = self.text.toPlainText().strip()
        if not text:
            QMessageBox.warning(self, "No Mizo text", "Paste some Mizo text first.")
            return

        sizes = [(1080,1350),(1080,1080),(1920,1080)]
        w,h = sizes[self.size_box.currentIndex()]
        pix = QPixmap(w,h)
        painter = QPainter(pix)

        gradients = [
            ((85,25,65),(220,75,120)),      # Romantic Sunset
            ((12,18,42),(105,35,75)),       # Midnight Rose
            ((55,35,90),(170,105,190)),     # Lavender
            ((65,38,12),(205,145,45)),      # Golden
            ((8,45,70),(45,145,175)),       # Ocean
            ((10,12,20),(70,30,55)),        # Dark
        ]
        a,b = gradients[self.style_box.currentIndex()]
        grad = QLinearGradient(0,0,w,h)
        grad.setColorAt(0,QColor(*a))
        grad.setColorAt(1,QColor(*b))
        painter.fillRect(0,0,w,h,QBrush(grad))

        # Decorative soft circles.
        painter.setOpacity(0.10)
        painter.setBrush(QBrush(QColor(255,255,255)))
        painter.setPen(Qt.NoPen)
        for x,y,r in [(int(w*.12),int(h*.16),150),(int(w*.88),int(h*.78),210),(int(w*.8),int(h*.12),90)]:
            painter.drawEllipse(x-r,y-r,2*r,2*r)
        painter.setOpacity(1.0)

        # Heart-like decorative symbols.
        painter.setPen(QPen(QColor(255,225,235), 2))
        painter.setFont(QFont("Segoe UI", 32))
        painter.drawText(0, 55, w, 50, Qt.AlignCenter, "♥  •  ♥")

        font_size = 54 if w == 1080 and h != 1080 else 50
        if w == 1920: font_size = 64
        font = QFont("Noto Sans", font_size, QFont.Bold)
        painter.setFont(font)
        painter.setPen(QPen(QColor(255,248,252), 1))
        rect = pix.rect().adjusted(90, 150, -90, -150)
        painter.drawText(rect, Qt.AlignCenter | Qt.TextWordWrap, text)

        painter.setFont(QFont("Segoe UI", 18))
        painter.setPen(QPen(QColor(255,235,245),1))
        painter.drawText(0,h-75,w,35,Qt.AlignCenter,"Mizo Love • Mizo only")

        painter.end()
        self.last_pixmap = pix

        preview = pix.scaled(
            self.preview.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.preview.setPixmap(preview)
        self.preview.setText("")

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if self.last_pixmap:
            self.preview.setPixmap(self.last_pixmap.scaled(
                self.preview.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def save_card(self):
        if self.last_pixmap is None:
            self.generate_card()
        if self.last_pixmap is None:
            return
        from PySide6.QtWidgets import QFileDialog
        filename, _ = QFileDialog.getSaveFileName(
            self, "Save Mizo Love Card", "mizo_love_card.png",
            "PNG Image (*.png)"
        )
        if filename:
            self.last_pixmap.save(filename, "PNG")

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mizo Love — Large Romance & Affection Library")
        self.resize(1250,820)
        self.setStyleSheet(STYLE)
        self.current=-1; self.indices=[]
        self.english_visible=True
        self.build()
        self.refresh()

    def build(self):
        root=QWidget(); self.setCentralWidget(root)
        out=QVBoxLayout(root); out.setContentsMargins(25,22,25,20); out.setSpacing(14)

        h=QHBoxLayout()
        box=QVBoxLayout()
        t=QLabel("❤️ Mizo Love"); t.setObjectName("title")
        s=QLabel("A larger Mizo romance & affection library — Mizo first, English for understanding")
        s.setObjectName("subtitle")
        box.addWidget(t); box.addWidget(s); h.addLayout(box); h.addStretch()
        self.random=QPushButton("✨ Random"); self.random.clicked.connect(self.random_phrase); h.addWidget(self.random)
        self.sources=QPushButton("📚 Sources"); self.sources.setObjectName("secondary"); self.sources.clicked.connect(self.show_sources); h.addWidget(self.sources)
        out.addLayout(h)

        bar=QHBoxLayout()
        self.search=QLineEdit(); self.search.setPlaceholderText("Search English or Mizo…"); self.search.textChanged.connect(self.refresh); bar.addWidget(self.search,1)
        self.cat=QComboBox(); self.cat.addItem("All categories")
        self.cat.addItems(sorted({x[0] for x in DATA})); self.cat.currentTextChanged.connect(self.refresh); bar.addWidget(self.cat)
        self.toggle=QPushButton("Hide English"); self.toggle.setObjectName("secondary"); self.toggle.clicked.connect(self.toggle_english); bar.addWidget(self.toggle)
        out.addLayout(bar)

        body=QHBoxLayout(); body.setSpacing(15)
        panel=QFrame(); panel.setObjectName("panel"); pl=QVBoxLayout(panel)
        self.count=QLabel(); self.count.setObjectName("subtitle"); pl.addWidget(self.count)
        self.list=QListWidget(); self.list.currentRowChanged.connect(self.select); pl.addWidget(self.list)
        panel.setMaximumWidth(410); body.addWidget(panel)

        right=QVBoxLayout()
        self.card=PhraseCard(); right.addWidget(self.card,1)
        nav=QHBoxLayout()
        self.prev=QPushButton("← Previous"); self.prev.setObjectName("secondary"); self.prev.clicked.connect(self.previous)
        self.next=QPushButton("Next →"); self.next.clicked.connect(self.next_phrase)
        self.copy=QPushButton("Copy Mizo"); self.copy.setObjectName("secondary"); self.copy.clicked.connect(self.copy_mizo)
        nav.addWidget(self.prev); nav.addWidget(self.next); nav.addStretch(); nav.addWidget(self.copy); right.addLayout(nav)
        body.addLayout(right,1); out.addLayout(body,1)

        # Integrated card generation section.
        self.generator = CardGenerator()
        out.addWidget(self.generator)

        foot=QLabel("⚠ Reference entries are source-backed; practice entries are prompts for translation and should be checked by a fluent Mizo speaker.")
        foot.setObjectName("subtitle"); foot.setAlignment(Qt.AlignCenter); out.addWidget(foot)

    def refresh(self):
        q=self.search.text().strip().lower(); c=self.cat.currentText()
        self.indices=[i for i,p in enumerate(DATA) if (not q or q in p[1].lower() or q in p[2].lower()) and (c=="All categories" or p[0]==c)]
        self.list.blockSignals(True); self.list.clear()
        for i in self.indices:
            p=DATA[i]; self.list.addItem(QListWidgetItem(f"{p[1]}\n{p[2]}"))
        self.list.blockSignals(False)
        self.count.setText(f"{len(self.indices)} expressions shown • {len(DATA)} total")
        if self.indices:
            self.list.setCurrentRow(0); self.select(0)
        else:
            self.card.show(("","No match","—","Try another search.","Practice"),self.english_visible)

    def select(self,row):
        if not self.indices or row<0 or row>=len(self.indices): return
        self.current=self.indices[row]; self.card.show(DATA[self.current],self.english_visible)

    def next_phrase(self):
        if not self.indices:return
        r=self.indices.index(self.current) if self.current in self.indices else 0
        self.list.setCurrentRow((r+1)%len(self.indices))

    def previous(self):
        if not self.indices:return
        r=self.indices.index(self.current) if self.current in self.indices else 0
        self.list.setCurrentRow((r-1)%len(self.indices))

    def random_phrase(self):
        if self.indices:self.list.setCurrentRow(random.randrange(len(self.indices)))

    def toggle_english(self):
        self.english_visible=not self.english_visible
        self.toggle.setText("Hide English" if self.english_visible else "Show English")
        if self.current>=0:self.card.show(DATA[self.current],self.english_visible)

    def copy_mizo(self):
        if self.current>=0 and DATA[self.current][2]!="—":
            QApplication.clipboard().setText(DATA[self.current][2])

    def show_sources(self):
        txt="MIZO LOVE — REFERENCE SOURCES\n\n"
        for n,u,d in SOURCES: txt += f"{n}\n{u}\n{d}\n\n"
        QMessageBox.information(self,"Sources",txt)

if __name__=="__main__":
    app=QApplication(sys.argv); app.setApplicationName("Mizo Love")
    app.setFont(QFont("Segoe UI",10))
    w=App(); w.show(); sys.exit(app.exec())
