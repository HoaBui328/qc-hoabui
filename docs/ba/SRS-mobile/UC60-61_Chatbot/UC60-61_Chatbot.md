# ĐẶC TẢ YÊU CẦU NGƯỜI SỬ DỤNG

**Tiêu đề:** UC60-61 — Chatbot Trợ lý Đầu Tư trên Mobile  
**Ngày tạo:** 06/05/2026  
**Phiên bản:** v1.5

| Thuộc tính              | Giá trị                              |
| ------------------------- | -------------------------------------- |
| BA phụ trách            | huyen.dinh2                            |
| Phân hệ                 | Ứng dụng Di động (Mobile App)        |
| Loại chức năng          | Tương tác AI — Hỗ trợ tra cứu        |
| Đối tượng thực hiện     | Cá nhân / Tổ chức                    |
| Giao diện               | Màn hình Mobile (Portrait)            |
| Ngày tạo                | 06/05/2026                             |
| Phiên bản               | v1.4                                   |

---

## UC60-61 — Chatbot Trợ lý Đầu Tư trên Mobile

### 1. Mô tả chức năng

- **Tên chức năng:** Chatbot Trợ lý Đầu Tư trên Mobile
- **Mô tả:** Nhóm chức năng cho phép cá nhân, tổ chức tương tác với Chatbot AI "Trợ lý Đầu Tư" để tra cứu thông tin đầu tư (thủ tục hành chính, khu công nghiệp, chính sách ưu đãi, tiến độ hồ sơ...) theo dạng hội thoại. Bao gồm: màn hình chào mừng với lời giới thiệu và disclaimer, luồng gửi/nhận tin nhắn dạng bubble, và chức năng đánh giá chất lượng phản hồi của bot.
- **Phân quyền:** Cá nhân/Tổ chức (đã đăng nhập). Hai nhóm đối tượng có cùng hành vi — không có sự phân biệt.
- **Phạm vi ngoài UC (Exclusions):** UC này KHÔNG bao gồm: quản lý/huấn luyện model AI, xem lịch sử hội thoại giữa các phiên (session), tải xuống nội dung hội thoại, chức năng gọi điện hay video call.
- **Truy cập chức năng:** Sidebar → "Chatbot hỗ trợ" hoặc Floating Widget ở màn hình Trang chủ.
- **Điều kiện tiên quyết (Preconditions):** Thiết bị có kết nối mạng ổn định, người dùng đã đăng nhập vào hệ thống.
- **Điều kiện kết thúc (Postconditions):** Người dùng nhận được phản hồi từ Chatbot (trong trường hợp lỗi hệ thống: người dùng thấy thông báo lỗi thay vì phản hồi). Việc gửi đánh giá chất lượng phản hồi là tuỳ chọn, phụ thuộc vào hành động của người dùng.
- **Chức năng đáp ứng usecase số:** UC60, UC61 (Phụ lục XIV)

---

### 2. Mô tả giao diện

#### 2.1 Màn hình Chatbot — Trạng thái Welcome (Chưa có hội thoại)

**Mô tả giao diện:**
Đây là màn hình hiển thị ngay khi người dùng mở Chatbot lần đầu trong phiên (chưa gõ câu hỏi nào). Header màu đỏ đậm hiển thị tên "Trợ lý Đầu Tư" kèm subtitle "Đang hoạt động". Vùng giữa màn hình hiển thị Avatar bot, tiêu đề chào mừng, mô tả năng lực bot, và một bubble tin nhắn chào từ bot. Thanh nhập liệu cố định ở cuối màn hình, phía trên có dòng disclaimer miễn trừ trách nhiệm.

---

**Khung Header:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Nút Quay lại (←) | Button (Icon) | — | — | — | **Quy tắc hành động:**<br>- Tap → Quay về màn hình trước. (Xem CMR-06) |
| 2 | Icon Avatar Bot | Image (Circle) | Icon Robot | — | — | **Quy tắc hiển thị:**<br>- Icon robot nhỏ, nằm bên trái tiêu đề header. Nền hình tròn màu đỏ đậm đậm hơn. |
| 3 | Tiêu đề Header | Label | "Trợ lý Đầu Tư" | — | — | **Quy tắc hiển thị:**<br>- Font đậm, màu trắng. Nằm bên phải icon avatar. |
| 4 | Subtitle trạng thái | Label | "Đang hoạt động" | — | — | **Quy tắc hiển thị:**<br>- Font nhỏ hơn tiêu đề, màu trắng/xám nhạt. Nằm ngay dưới tiêu đề "Trợ lý Đầu Tư".<br>- **Trạng thái bình thường:** Hiển thị "Đang hoạt động".<br>- **Trạng thái lỗi hệ thống / không kết nối được API ngay khi mở màn hình:** Hiển thị "Chưa hoạt động" → Toàn bộ vùng nội dung bị thay thế bằng màn hình lỗi (xem mô tả Section 2.3). |

---

**Khung Welcome — Vùng giới thiệu bot:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 5 | Avatar Bot lớn | Image (Circle) | Icon Robot | — | — | **Quy tắc hiển thị:**<br>- Hình tròn lớn, nền hồng nhạt (màu pastel đỏ), icon robot màu đỏ đậm ở giữa.<br>- Căn giữa màn hình. |
| 6 | Tiêu đề chào mừng | Label | "Chào mừng bạn đến với Trợ lý Đầu Tư." | — | — | **Quy tắc hiển thị:**<br>- Font đậm, căn giữa. Hiển thị 2 dòng nếu cần (không truncate). |
| 7 | Câu hỏi mời tương tác | Label | "Bạn cần hỗ trợ gì?" | — | — | **Quy tắc hiển thị:**<br>- Font vừa, căn giữa, màu đen/xám đen. Nằm ngay dưới tiêu đề chào mừng. |
| 8 | Mô tả năng lực bot | Label (Multiline) | "Trợ lý Đầu Tư có thể hỗ trợ bạn: hỏi đáp chính sách pháp luật đầu tư, tra cứu quy trình thủ tục, hướng dẫn chuẩn bị hồ sơ, đánh giá sơ bộ điều kiện đầu tư, gợi ý phương án đầu tư, theo dõi nghĩa vụ sau cấp phép và kết nối hỗ trợ khi cần." | — | — | **Quy tắc hiển thị:**<br>- Font nhỏ, màu xám, căn giữa. Hiển thị full text, không truncate. |
| 9 | Bubble tin nhắn chào | Chat Bubble (Left) | "Chào mừng bạn đến với Trợ lý Đầu Tư. Bạn cần hỗ trợ gì?" | — | — | **Quy tắc hiển thị:**<br>- Bubble nằm bên trái (tin nhắn của bot). Nền xám nhạt, bo góc.<br>- Đây là tin nhắn mặc định được hiển thị sẵn khi mở màn hình — không do người dùng gửi.<br>- **Trạng thái ẩn:** Sau khi người dùng gửi câu hỏi đầu tiên (hội thoại bắt đầu), toàn bộ vùng Welcome (avatar lớn, tiêu đề, mô tả, bubble chào) bị ẩn. Vùng hội thoại chiếm toàn bộ màn hình. |

---

**Khung Input Bar (Cố định ở cuối màn hình):**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 10 | Disclaimer miễn trừ trách nhiệm | Label | "Thông tin Trợ lý AI cung cấp chỉ mang tính hỗ trợ. Vui lòng kiểm tra nội dung quan trọng" | — | — | **Quy tắc hiển thị:**<br>- Nằm cố định phía trên ô nhập liệu, luôn hiển thị ở cả trạng thái Welcome lẫn trạng thái Hội thoại.<br>- Font nhỏ, màu xám, căn giữa. Không truncate. |
| 11 | Ô nhập câu hỏi | Textbox (Chat) | "Nhập câu hỏi về đầu tư" | x | — | **Quy tắc hiển thị:**<br>- Placeholder: "Nhập câu hỏi về đầu tư". Nền xám nhạt, bo góc pill.<br>- Hiển thị tối đa 5 dòng; khi nội dung vượt quá 5 dòng thì cuộn được trong ô (scroll nội bộ).<br>- Giới hạn tối đa **255 ký tự**. Chấp nhận mọi loại ký tự. Khi vượt quá 255 ký tự, hiển thị lỗi inline: `"Câu hỏi không được vượt quá 255 ký tự!"`.<br><br>**Quy tắc hành động:**<br>- Tap vào ô → Bàn phím hiển thị, con trỏ nhấp nháy trong ô.<br>- Tap ra ngoài ô (out-tap) → Bàn phím đóng lại, ô mất focus. Nội dung đã nhập được giữ nguyên. Hệ thống tự động xóa khoảng trắng đầu/cuối khi out-tap.<br>- **Exception CMR-09:** Ô nhập chatbot **không validate on blur** — chỉ validate khi tap nút Gửi. Lý do: UX chatbot không nên hiện lỗi mỗi khi user tap ra ngoài ô nhập liệu.<br>- Sau khi gửi tin nhắn thành công → Ô nhập liệu xóa trắng, bàn phím **vẫn giữ nguyên** (không đóng). Bàn phím chỉ đóng khi out-tap.<br>- **Khi nút Gửi đang ở trạng thái Loading:** Ô nhập liệu vẫn cho phép nhập ký tự, nhưng không thể gửi tin nhắn mới cho đến khi bot phản hồi xong. |
| 12 | Nút Gửi (Send) | Button (Icon) | — | — | — | **Quy tắc hiển thị:**<br>- **Trạng thái mặc định (ô trống):** Luôn hiển thị. Icon paper plane màu xám, nền hình tròn xám nhạt (enabled nhưng inactive style).<br>- **Trạng thái có nội dung:** Icon paper plane màu trắng, nền hình tròn đỏ đậm (active style).<br>- **Trạng thái Loading (sau khi gửi):** Đổi sang icon spinner (vòng tròn xoay), nền xám. Không nhận thêm input mới trong thời gian bot đang xử lý.<br><br>**Quy tắc hành động:**<br>- Tap khi ô trống → Validate → Hiển thị lỗi inline: `"Vui lòng nhập Câu hỏi"`.<br>- Tap khi có nội dung hợp lệ → Gửi câu hỏi, nút chuyển sang trạng thái Loading cho đến khi nhận được phản hồi từ bot. |

#### 2.2 Màn hình Chatbot — Trạng thái Hội thoại (Đang chat)

**Mô tả giao diện:**
Sau khi người dùng gửi câu hỏi đầu tiên, vùng Welcome bị ẩn. Màn hình hiển thị toàn bộ lịch sử hội thoại dạng bubble. Bubble người dùng nằm bên phải; bubble bot nằm bên trái. Dưới mỗi phản hồi của bot có thanh đánh giá "Đánh giá câu trả lời:". Input bar vẫn cố định ở cuối màn hình như mục 2.1.

---

**Khung Vùng Hội thoại:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 13 | Bubble tin nhắn người dùng | Chat Bubble (Right) | — | — | — | **Quy tắc hiển thị:**<br>- Nằm bên phải màn hình. Nền xám nhạt, bo góc.<br>- Tin nhắn dài hiển thị full, không truncate.<br>- Không có nút đánh giá hay hành động kèm theo.<br>- Không hỗ trợ nhấn giữ để sao chép nội dung. |
| 14 | Bubble phản hồi Bot | Chat Bubble (Left) | — | — | — | **Quy tắc hiển thị:**<br>- Nằm bên trái màn hình. Nền trắng/xám nhạt, bo góc.<br>- Tin nhắn dài hiển thị full, không truncate. Hỗ trợ xuống dòng tự nhiên.<br>- Chỉ hỗ trợ plain text và danh sách (bullet list / numbered list). Không hỗ trợ in đậm, in nghiêng, gạch chân, hyperlink.<br>- AI chỉ phản hồi dạng: plain text và danh sách (không có hình ảnh, không có video, không có file đính kèm).<br>- Phía dưới mỗi bubble bot hiển thị thanh "Đánh giá câu trả lời" (xem field #16).<br>- Không hỗ trợ nhấn giữ để sao chép nội dung. |
| 15 | Typing Indicator (Bot đang trả lời) | Animation (3 dots) | — | — | — | **Quy tắc hiển thị:**<br>- Hiển thị khi hệ thống đang chờ phản hồi từ API Chatbot.<br>- Dạng 3 chấm nhảy (bouncing dots) nằm trong bubble trái.<br>- Tự động ẩn khi phản hồi được nhận và hiển thị. |

---

**Khung Đánh giá phản hồi (UC61 — Dưới mỗi bubble bot):**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 16 | Nhãn "Đánh giá câu trả lời:" | Label | "Đánh giá câu trả lời:" | — | — | **Quy tắc hiển thị:**<br>- Font nhỏ, màu đỏ đậm, nằm bên trái thanh đánh giá, ngay dưới bubble bot tương ứng. |
| 17 | Nút Thumbs Up (👍) | Button (Icon) | — | — | — | **Quy tắc hiển thị:**<br>- **Trạng thái chưa đánh giá:** Hiển thị icon 👍 và icon 👎 — cả hai màu xám.<br>- **Trạng thái đang chọn (animation):** Khi tap/nhấn giữ → Icon 👍 chuyển sang fill đỏ đậm (toàn bộ icon được tô đỏ) trong chốc lát.<br>- **Trạng thái đã đánh giá:** Ẩn 2 icon, thay bằng text *"Bạn đã đánh giá câu trả lời. **Đánh giá lại?**"* ("Đánh giá lại?" là link màu đỏ đậm, có thể tap).<br><br>**Quy tắc hành động:**<br>- Tap 👍 → Icon 👍 fill đỏ đậm (animation ngắn) → Chuyển sang trạng thái đã đánh giá + gửi API (UC61).<br>- Tap "Đánh giá lại?" → Quay về UI gốc (2 icon xám). |
| 18 | Nút Thumbs Down (👎) | Button (Icon) | — | — | — | **Quy tắc hiển thị:**<br>- **Trạng thái chưa đánh giá:** Hiển thị icon 👎 và icon 👍 — cả hai màu xám.<br>- **Trạng thái đang chọn (animation):** Khi tap/nhấn giữ → Icon 👎 chuyển sang fill đỏ đậm (toàn bộ icon được tô đỏ) trong chốc lát.<br>- **Trạng thái đã đánh giá:** Ẩn 2 icon, thay bằng text *"Bạn đã đánh giá câu trả lời. **Đánh giá lại?**"* ("Đánh giá lại?" là link màu đỏ đậm, có thể tap).<br><br>**Quy tắc hành động:**<br>- Tap 👎 → Icon 👎 fill đỏ đậm (animation ngắn) → Chuyển sang trạng thái đã đánh giá + gửi API (UC61).<br>- Tap "Đánh giá lại?" → Quay về UI gốc (2 icon xám). |


---

#### 2.3 Màn hình Chatbot — Trạng thái Offline (Không hoạt động)

**Mô tả giao diện:**
Khi mở Chatbot mà hệ thống không call được API (offline hoặc lỗi hệ thống), Header vẫn hiển thị bình thường nhưng subtitle đổi thành "Chưa hoạt động". Toàn bộ vùng nội dung trống, hiển thị thông báo lỗi ở giữa màn hình.

---

**Khung Thông báo Offline:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 19 | Icon trạng thái | Image (Icon) | Icon wifi bị gạch chéo | — | — | **Quy tắc hiển thị:**<br>- Icon wifi gạch chéo, màu xám, nền hình tròn xám nhạt, căn giữa màn hình. |
| 20 | Tiêu đề lỗi | Label | "Chatbot tạm thời chưa hoạt động" | — | — | **Quy tắc hiển thị:**<br>- Font đậm, căn giữa, màu đen. Nằm ngay dưới icon. |
| 21 | Mô tả hướng dẫn | Label | "Vui lòng quay lại sau hoặc liên hệ quản trị hệ thống để được hỗ trợ." | — | — | **Quy tắc hiển thị:**<br>- Font nhỏ, màu xám, căn giữa. Nằm ngay dưới tiêu đề lỗi. |
| 22 | Nút Thử lại | Button | "Thử lại" | — | — | **Quy tắc hành động:**<br>- Tap → Gọi lại API kiểm tra kết nối. Nếu thành công → Chuyển sang trạng thái Welcome. Nếu vẫn lỗi → Giữ nguyên màn hình này. |

---

### 3. Mô tả các xử lý của chức năng

#### 3.1 Luồng gửi câu hỏi và nhận phản hồi (UC60)

1. Người dùng mở Chatbot → Hiển thị trạng thái **Welcome**.
2. Người dùng nhập câu hỏi vào ô nhập liệu.
3. Người dùng tap nút **Gửi**.
4. Hệ thống thực hiện đồng thời:
   - Hiển thị bubble người dùng bên phải ngay lập tức.
   - Ẩn vùng Welcome (nếu đây là câu hỏi đầu tiên trong phiên).
   - Xóa trắng ô nhập liệu. **Bàn phím giữ nguyên** (không đóng sau khi gửi).
   - Nút Gửi chuyển sang trạng thái **Loading** (spinner xám). Không nhận prompt mới.
   - Hiển thị **Typing Indicator** (3 chấm nhảy) bên trái.
5. Hệ thống gọi API Chatbot.
6. Khi API phản hồi: Ẩn Typing Indicator → Nút Gửi về trạng thái bình thường → Hiển thị bubble bot bên trái kèm thanh đánh giá (👍 / 👎).
7. **Auto-scroll:** Sau khi bubble bot hiển thị xong (không phải trong lúc typing), màn hình tự cuộn xuống tin nhắn mới nhất — kể cả khi người dùng đang cuộn lên xem lịch sử.
8. **Lazy load lịch sử:** Khi kéo lên đầu danh sách tin nhắn mà chưa tải hết → Hiển thị loading ở trên cùng, sau đó tải thêm tin nhắn cũ. **Exception CMR-04:** Số lượng tải mỗi lần do API AI Chatbot quyết định (không cố định 20 items) vì chatbot history có cơ chế quản lý pagination riêng. Khi tải lỗi → tự động retry 3 lần (CMR-04). Sau 3 lần fail → dừng, hiển thị thông báo lỗi cục bộ.
9. **Pull-to-Refresh (CMR-13):** Khi người dùng kéo xuống từ đầu màn hình chat (đã scroll lên trên cùng và không còn lịch sử chat cũ hơn để tải) → trigger refresh dữ liệu. Hiển thị spinner trong khi đang refresh. Sau khi refresh thành công → cập nhật danh sách tin nhắn.

#### 3.2 Luồng đánh giá phản hồi Chatbot (UC61)

1. Người dùng tap 👍 hoặc 👎 dưới bubble bot.
2. Hệ thống gửi đánh giá qua API (kèm ID phản hồi).
3. 2 icon ẩn đi, thay bằng text *"Bạn đã đánh giá câu trả lời. **Đánh giá lại?**"* ("Đánh giá lại?" là link đỏ đậm).
4. Tap **"Đánh giá lại?"** → Hệ thống gọi API để reset đánh giá → Quay về UI gốc (hiển thị lại 2 icon 👍 👎).

#### 3.3 Quy tắc phiên hội thoại

- **Không lưu lịch sử giữa các phiên:** Mỗi lần mở lại màn hình Chatbot, hội thoại bắt đầu từ đầu — hiển thị lại trạng thái Welcome.
- **Hội thoại trong phiên:** Tất cả tin nhắn trong phiên được giữ khi cuộn lên xem lịch sử.
- **Thoát giữa chừng (Back):** Khi người dùng nhấn Back trong khi đang có hội thoại → Hiển thị popup xác nhận:
  - Tiêu đề: *"Rời khỏi cuộc trò chuyện?"*
  - Nội dung: *"Đoạn hội thoại không được lưu trữ. Bạn có chắc muốn rời chatbot không?"*
  - Nút **"Ở lại"** (Secondary) → Đóng popup, quay lại hội thoại.
  - Nút **"Rời chatbot"** (Primary đỏ) → Thoát màn hình Chatbot.
  - Nếu chưa có hội thoại nào (trạng thái Welcome) → Back trực tiếp, không hiện popup.

#### 3.4 Xử lý lỗi (Tham chiếu CMR-07)

| Tình huống lỗi | Thông báo hiển thị | Hành vi hệ thống |
| --- | --- | --- |
| Lỗi mạng khi gửi câu hỏi | *"Không thể kết nối. Vui lòng kiểm tra mạng và thử lại"* (CMR-07) | Ẩn Typing Indicator. Nút Gửi về bình thường. Hiển thị Toast lỗi. Trả lại nội dung tin nhắn vừa gửi vào ô nhập liệu để người dùng có thể gửi lại. |
| API Chatbot thất bại (HTTP 500) | *"Hệ thống đang bận. Vui lòng thử lại sau"* (CMR-07) | Ẩn Typing Indicator. Nút Gửi về bình thường. Hiển thị Toast lỗi. Trả lại tin nhắn về ô nhập liệu. |
| API timeout (>30 giây) | *"Yêu cầu đã hết thời gian chờ. Vui lòng thử lại"* (CMR-07) | Ẩn Typing Indicator. Nút Gửi về bình thường. Toast lỗi + nút "Thử lại". Trả lại tin nhắn về ô. **Lý do timeout 30 giây:** API Chatbot AI cần thời gian xử lý ngôn ngữ tự nhiên và truy vấn knowledge base, thời gian phản hồi trung bình dài hơn API thông thường. |
| Lỗi 401 (Session hết hạn) | *"Phiên đăng nhập hết hạn"* (Toast) | Hệ thống tự động sử dụng refresh token để cấp lại access token mới. Nếu refresh token đã hết hạn hoặc không hợp lệ (quá 15 ngày) → chuyển về màn hình Đăng nhập. (Xem CMR-07) |
| Chatbot không hiểu câu hỏi (fallback) | *"Xin lỗi, tôi chưa hiểu câu hỏi của bạn. Vui lòng thử diễn đạt cách khác"* | Hiển thị bubble bot bình thường với nội dung fallback. Có thanh đánh giá bên dưới. |
| Câu hỏi ngoài phạm vi đầu tư (NN_50) | *"Câu hỏi nằm ngoài phạm vi đầu tư. Vui lòng liên hệ hotline (+84) 24 2220 2828 để được hỗ trợ"* | Hiển thị bubble bot bình thường với nội dung từ chối kèm thông tin hotline. Có thanh đánh giá bên dưới. |
| Gửi đánh giá thất bại | — | Không thay đổi UI. Thử lại ngầm. |
| Chatbot offline (không call được API khi mở màn hình) | — | Subtitle đổi "Chưa hoạt động". Hiển thị màn hình lỗi (Section 2.3): icon + text + nút "Thử lại". |
| Offline khi mở app | — | Xử lý theo CMR-07. |

#### 3.5 Tiêu chí chấp nhận (Acceptance Criteria)

- **AC1:** Mở Chatbot → Hiển thị trạng thái Welcome với avatar, lời chào, mô tả năng lực bot và disclaimer cố định phía trên ô nhập liệu.
- **AC2:** Gửi câu hỏi → Bubble người dùng hiển thị ngay. Nút Gửi chuyển Loading. Bàn phím không đóng. Typing Indicator xuất hiện. Sau khi nhận phản hồi → Typing Indicator ẩn, bubble bot hiển thị, nút Gửi về bình thường.
- **AC3:** Ô nhập liệu giới hạn tối đa 255 ký tự. Khi vượt quá hiển thị lỗi inline `"Câu hỏi không được vượt quá 255 ký tự!"`. Hiển thị tối đa 5 dòng, cuộn nội bộ khi vượt quá. Tap ngoài → bàn phím đóng. Nút Gửi luôn hiển thị enabled; tap khi ô trống → hiển thị lỗi `"Vui lòng nhập Câu hỏi"`.
- **AC4:** Tap 👍 hoặc 👎 → 2 icon ẩn, hiển thị text "Bạn đã đánh giá câu trả lời. Đánh giá lại?". Tap "Đánh giá lại?" → Quay về 2 icon.
- **AC5:** Sau khi bubble bot hiển thị xong → Màn hình tự cuộn đến tin nhắn mới nhất (dù đang cuộn lên xem lịch sử).
- **AC6:** Back trong khi có hội thoại → Hiện popup "Rời khỏi cuộc trò chuyện?". Tap "Ở lại" → đóng popup. Tap "Rời chatbot" → thoát màn hình.
- **AC7:** Mở lại Chatbot → Trở về trạng thái Welcome (không có lịch sử phiên trước).
- **AC8:** Lỗi API → Typing Indicator ẩn, Toast lỗi hiển thị đúng thông báo CMR-07. Tin nhắn vừa gửi được trả về ô nhập liệu.
- **AC9:** Mở Chatbot khi offline → Subtitle hiển thị "Chưa hoạt động", màn hình lỗi hiển thị icon + text + nút "Thử lại". Tap "Thử lại" → gọi lại API.
- **AC10:** Câu hỏi ngoài phạm vi đầu tư → Bot phản hồi message từ chối kèm hotline (+84) 24 2220 2828.
- **AC11:** Disclaimer "Thông tin Trợ lý AI cung cấp chỉ mang tính hỗ trợ. Vui lòng kiểm tra nội dung quan trọng" luôn hiển thị cố định phía trên ô nhập liệu ở mọi trạng thái.

#### 3.6 Đa ngôn ngữ (→ Xem CMR-17)

Toàn bộ text cứng trên màn hình UC60-61 (header, subtitle trạng thái, tiêu đề chào mừng, mô tả năng lực bot, disclaimer, placeholder ô nhập liệu, nhãn đánh giá, thông báo lỗi, nút "Thử lại", popup xác nhận rời chatbot) được dịch sang ngôn ngữ hiển thị tương ứng khi người dùng đổi ngôn ngữ. Hỗ trợ 5 ngôn ngữ: VI, EN, ZH, JA, KO.

**Logic ngôn ngữ phản hồi AI:** Khi người dùng chọn ngôn ngữ hệ thống là A nhưng nhập câu hỏi bằng ngôn ngữ B, hệ thống tự động nhận diện ngôn ngữ đầu vào và phản hồi theo ngôn ngữ câu hỏi (ngôn ngữ B).

---

## 4. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-11 | v1 → v1.1 | 3.4 Xử lý lỗi — HTTP 401 | (Không có) | Bổ sung xử lý lỗi 401: auto refresh token, nếu hết hạn >15 ngày → redirect đăng nhập + toast "Phiên đăng nhập hết hạn." | Đồng bộ CMR-07 (B1) |
| 2026-05-11 | v1 → v1.1 | 3.6 Đa ngôn ngữ | (Không có) | Bổ sung section đa ngôn ngữ: text cứng dịch 5 ngôn ngữ (VI, EN, ZH, JA, KO), nội dung AI/chip giữ nguyên | Đồng bộ CMR-17 (B2) |
| 2026-05-11 | v1 → v1.1 | 2.1 Field #10 — Debounce Navigation | (Không có) | Tap nhanh liên tục vào chip gợi ý → chỉ nhận action đầu tiên, bỏ qua tap tiếp theo cho đến khi xử lý hoàn tất | Đồng bộ CMR-18 (B3) |
| 2026-05-11 | v1 → v1.1 | 3.4 Timeout — Ghi lý do 30 giây | Timeout 30 giây (không ghi lý do) | Bổ sung lý do: API Chatbot AI cần thời gian xử lý NLP và truy vấn knowledge base, thời gian phản hồi trung bình dài hơn API thông thường | Đồng bộ B5 |
| 2026-05-12 | v1.1 → v1.2 | Bổ sung CMR-13 (Pull-to-Refresh) | (Không có) | Pull-to-refresh khi kéo lên trên cùng (không còn lịch sử) | Đồng bộ Cross-UC Inconsistency Report v2 |
| 2026-05-14 | v1.2 → v1.3 | 2.1 Field #10 — Xóa chip gợi ý | Danh sách chip gợi ý câu hỏi nhanh (dynamic từ API, tap auto-sends, debounce CMR-18) | (Đã xóa) | Theo Q&A confirm: bỏ chip gợi ý |
| 2026-05-14 | v1.2 → v1.3 | 2.2 Field #16 — Xóa file đính kèm | File đính kèm trong Bubble Bot (PDF mở browser, DOCX download, CMR-08) | (Đã xóa) | Theo Q&A confirm: chatbot chỉ phản hồi text |
| 2026-05-14 | v1.2 → v1.3 | 2.2 Field #15 — Rich text → Plain text | Hỗ trợ rich text: in đậm, in nghiêng, gạch chân, hyperlink | Chỉ hỗ trợ plain text và danh sách (bullet/numbered list). Không bold/italic/underline/hyperlink | Theo Q&A confirm: chỉ phản hồi text |
| 2026-05-14 | v1.2 → v1.3 | 2.1 Input Bar — Bổ sung Disclaimer | (Không có) | Field #10: Disclaimer "Thông tin Trợ lý AI cung cấp chỉ mang tính hỗ trợ..." cố định phía trên ô nhập liệu, luôn hiển thị | Theo NN_52 + Q&A confirm |
| 2026-05-14 | v1.2 → v1.3 | 3.4 — Bổ sung case "Ngoài phạm vi" | (Không có) | Câu hỏi ngoài phạm vi đầu tư → Bot phản hồi: "Câu hỏi nằm ngoài phạm vi đầu tư. Vui lòng liên hệ hotline (+84) 24 2220 2828 để được hỗ trợ." | Theo NN_50 + NN_48 |
| 2026-05-14 | v1.2 → v1.3 | 3.6 — Sửa logic ngôn ngữ phản hồi AI | Nội dung AI hiển thị nguyên bản — không thay đổi theo ngôn ngữ | Khi user nhập ngôn ngữ B (khác ngôn ngữ hệ thống A), bot tự động detect và trả lời theo ngôn ngữ câu hỏi (ngôn ngữ B) | Theo Q&A confirm NN_47 |
| 2026-05-14 | v1.2 → v1.3 | 2.1 Field #8 — Cập nhật mô tả năng lực bot | "giải đáp mọi thông tin về đầu tư bao gồm: thủ tục hành chính, khu công nghiệp, chính sách ưu đãi, tra cứu tiến độ hồ sơ..." | "hỏi đáp chính sách pháp luật đầu tư, tra cứu quy trình thủ tục, hướng dẫn chuẩn bị hồ sơ, đánh giá sơ bộ điều kiện đầu tư, gợi ý phương án đầu tư, theo dõi nghĩa vụ sau cấp phép và kết nối hỗ trợ khi cần" | Đồng bộ NN_46 (phạm vi hỗ trợ) |
| 2026-05-21 | v1.3 → v1.4 | 2.1 Field #11 — Placeholder | `"Nhập câu hỏi về đầu tư..."` | `"Nhập câu hỏi về đầu tư"` (bỏ dấu `...`) | Đồng bộ CMR E05 / A05 |
| 2026-05-21 | v1.3 → v1.4 | 2.1 Field #11 — Max length | 500 ký tự, chặn nhập khi đạt max | 255 ký tự (rule chung G01). Khi vượt quá hiển thị lỗi inline: `"Câu hỏi không được vượt quá 255 ký tự!"` | Đồng bộ CMR G01 / A07 / H03 |
| 2026-05-21 | v1.3 → v1.4 | 2.1 Field #12 — Nút Gửi | Ẩn khi ô nhập liệu trống. Tap → gửi câu hỏi | Luôn hiển thị enabled. Tap khi trống → validate → lỗi `"Vui lòng nhập Câu hỏi"`. Tap khi có nội dung → gửi câu hỏi | Đồng bộ CMR I01 / H01 |
| 2026-05-21 | v1.3 → v1.4 | 3.5 AC3 | Ô nhập liệu giới hạn tối đa 500 ký tự. Hiển thị tối đa 5 dòng, cuộn nội bộ khi vượt quá. Tap ngoài → bàn phím đóng | Ô nhập liệu giới hạn tối đa 255 ký tự. Khi vượt quá hiển thị lỗi inline. Nút Gửi luôn hiển thị enabled; tap khi ô trống → hiển thị lỗi | Đồng bộ CMR G01 / I01 |
| 2026-05-22 | v1.4 → v1.5 | §3.4 — Toast/Error messages | Các message có dấu `.` cuối: "...thử lại.", "...thử lại sau.", "...hết hạn.", "...cách khác.", "...hỗ trợ." | Bỏ dấu `.` cuối tất cả toast/error/bubble bot messages | Cascade từ CMR-07 v1.13 — thống nhất bỏ dấu `.` |
| 2026-05-22 | v1.4 → v1.5 | §3.1 step 8 — Lazy load lịch sử | "Số lượng tải mỗi lần do API AI Chatbot quyết định" (không ghi exception, không có retry) | Bổ sung Exception CMR-04: pagination do API Chatbot quyết định. Bổ sung retry 3 lần khi tải lỗi (CMR-04) | Align CMR-04 |
| 2026-05-22 | v1.4 → v1.5 | §2.1 Field #11 — Validate on blur | Không mô tả hành vi validate on blur | Bổ sung Exception CMR-09: Ô nhập chatbot không validate on blur, chỉ validate khi tap nút Gửi | Align CMR-09 — UX exception cho chatbot |
