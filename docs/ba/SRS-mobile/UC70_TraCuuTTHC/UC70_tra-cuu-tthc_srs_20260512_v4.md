# ĐẶC TẢ YÊU CẦU NGƯỜI SỬ DỤNG
**Tiêu đề:** UC70 — Tra cứu thủ tục hành chính trên Mobile  
**Ngày tạo:** 12/05/2026  
**Phiên bản:** v4.0

| Thuộc tính | Giá trị |
|---|---|
| BA phụ trách | hieu.luu2 |
| Phân hệ | Ứng dụng Di động (Mobile App) |
| Loại chức năng | Tra cứu thông tin thủ tục hành chính |
| Đối tượng thực hiện | Cá nhân / Tổ chức |
| Giao diện | Màn hình Mobile (Portrait) |
| Ngày tạo | 12/05/2026 |
| Phiên bản | v4.0 |

---

## UC70 — Tra cứu thủ tục hành chính trên Mobile

### 1. Mô tả chức năng

- **Tên chức năng:** Tra cứu thủ tục hành chính trên Mobile
- **Mô tả:** Chức năng cho phép cá nhân, tổ chức tra cứu, xem danh sách và xem chi tiết các thủ tục hành chính. Người dùng có thể tìm kiếm theo mã, tên dịch vụ công; sử dụng bộ lọc (lĩnh vực, ngôn ngữ); và xem chi tiết thủ tục được tổ chức theo 5 tab nội dung: Thông tin chung, Trình tự thực hiện, Thành phần hồ sơ, Cách thức thực hiện, Căn cứ pháp lý.
- **Phân quyền:** Cá nhân/Tổ chức (không yêu cầu đăng nhập — public access).
- **Phạm vi ngoài UC (Exclusions):** UC70 KHÔNG bao gồm chức năng nộp hồ sơ thủ tục trực tuyến (được quy định ở UC khác nếu có).
- **Truy cập chức năng:** Trang chủ → "Thủ tục hành chính" (Tham chiếu UC1 — Trang chủ Dashboard) hoặc Sidebar → "Thủ tục hành chính".
- **Điều kiện tiên quyết (Preconditions):**
  - Thiết bị có kết nối mạng ổn định.
- **Điều kiện kết thúc (Postconditions):** Hệ thống hiển thị kết quả danh sách thủ tục hành chính theo điều kiện tìm kiếm/lọc hoặc hiển thị thông tin chi tiết của thủ tục được chọn.
- **Chức năng đáp ứng usecase số:** UC70

---

### 2. Mô tả giao diện

#### 2.1 Màn hình Danh sách Thủ tục hành chính

**Mô tả giao diện:**
Header "Thủ tục hành chính" (màu đỏ đậm, có icon thông báo). Bên dưới là ô tìm kiếm và nút Bộ lọc. Cuối cùng là danh sách kết quả dạng List Card dọc.

**Khung Header & Tìm kiếm:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Nút Quay lại (←) | Button (Icon) | — | — | — | **Quy tắc hành động:**<br>- Tap → Quay về màn hình trước. (Xem CMR-06) |
| 2 | Tiêu đề Header | Label | "Thủ tục hành chính" | — | — | **Quy tắc hiển thị:**<br>- Nằm giữa header, màu trắng trên nền đỏ đậm. |
| 3 | Icon Thông báo | Button (Icon) | — | — | — | **Quy tắc hiển thị:**<br>- Nằm góc phải của header (icon chuông có chấm đỏ).<br>**Quy tắc hành động:**<br>- Tap → Chuyển đến màn hình Thông báo. |
| 4 | Ô tìm kiếm | Textbox (Search) | "Tìm kiếm nhanh theo mã, tên dịch vụ công" | x | — | **Quy tắc hiển thị:**<br>- Nền trắng, viền xám mỏng. Placeholder: "Tìm kiếm nhanh theo mã, tên dịch vụ công".<br>- Tối đa **500 ký tự** (Xem CMR-01).<br><br>**Quy tắc hành động:**<br>- Nhập từ khóa → Hệ thống tìm kiếm theo tên hoặc mã thủ tục. Kết quả tự động cập nhật sau debounce 3 giây (Tham khảo CMR-01).<br>- Xử lý whitespace: auto-trim khoảng trắng đầu/cuối trước khi tìm kiếm. Nếu sau trim rỗng → coi như input rỗng (Xem CMR-01).<br>- Xóa hết từ khóa → Hiển thị danh sách mặc định.<br>- State Persistence: Sau khi vào chi tiết và quay lại, danh sách giữ nguyên trạng thái tìm kiếm/lọc trước đó (CMR-01). |
| 5 | Nút "Lọc" | Button (Icon) | — | — | — | **Quy tắc hiển thị:**<br>- Icon filter, nằm bên phải ô tìm kiếm.<br>- **Active filter indicator:** Khi đang có bộ lọc được áp dụng (Lĩnh vực hoặc Ngôn ngữ khác mặc định), hiển thị chấm xanh (indicator) trên icon báo hiệu trạng thái đang lọc (Xem CMR-02).<br><br>**Quy tắc hành động:**<br>- Tap → Mở Modal popup "Bộ lọc tìm kiếm". |

**Khung Danh sách kết quả:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 6 | Danh sách Card thủ tục | List Card (Vertical) | — | — | — | **Quy tắc hiển thị:**<br>- Danh sách cuộn dọc. Hỗ trợ lazy load / infinite scroll (tải 20 bản ghi/lần).<br>- **Trạng thái Empty (Không có kết quả):** Nếu không tìm thấy, hiển thị *"Không tìm thấy kết quả."* (Tham chiếu CMR-14).<br><br>**Quy tắc hành động:**<br>- Hỗ trợ Pull to Refresh (CMR-13) để tải lại danh sách. |
| 7 | Tên thủ tục | Label (H3) | — | — | — | **Quy tắc hiển thị:**<br>- Font đậm, màu đen, tối đa 2 dòng, nằm trên cùng của thẻ. (VD: "Thủ tục đăng ký đầu tư dự án mới"). |
| 8 | Các thuộc tính thẻ | Label / Value | — | — | — | **Quy tắc hiển thị:**<br>Hiển thị danh sách các thuộc tính theo cặp nhãn - giá trị:<br>- **Mã thủ tục:** (VD: TT-001-2024)<br>- **Lĩnh vực:** (VD: Đầu tư)<br>- **Cơ quan:** (VD: Bộ Kế hoạch và Đầu tư)<br>Tất cả text nếu dài quá sẽ hiển thị `...`. Nếu null hiển thị "-". |
| 9 | Nút Xem chi tiết (Tap Card) | Interaction | — | — | — | **Quy tắc hành động:**<br>- Tap vào toàn bộ Card → Chuyển đến màn hình Chi tiết thủ tục.<br>- **Debounce Navigation (CMR-18):** Khi người dùng tap nhanh liên tục, hệ thống chỉ nhận action đầu tiên và bỏ qua các tap tiếp theo cho đến khi điều hướng hoàn tất. |

---

#### 2.2 Bottom Sheet Bộ lọc tìm kiếm

**Mô tả giao diện:**
Hiển thị dạng Bottom Sheet. Tap ra ngoài hoặc tap icon (X) đều đóng Bottom Sheet lại mà không áp dụng bộ lọc. 

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Nút Đóng (X) & Tiêu đề | Button (Icon) & Label | "Bộ lọc tìm kiếm" | — | — | **Quy tắc hiển thị:** Tiêu đề ở giữa, nút (X) ở góc phải.<br>**Quy tắc hành động:**<br>- Tap (X) hoặc tap ngoài vùng Bottom Sheet → Đóng, không áp dụng bộ lọc.<br>- Nhấn nút Back vật lý (Android) → Đóng Bottom Sheet. |
| 2 | Lĩnh vực | Dropdown (Single) | "Tất cả lĩnh vực" | x | — | **Quy tắc hiển thị:**<br>- List options trả về từ API. Mặc định "Tất cả lĩnh vực". |
| 3 | Ngôn ngữ | Dropdown (Single) | "Tiếng Việt" | x | — | **Quy tắc hiển thị:**<br>- List options trả về từ API hoặc list tĩnh. Mặc định "Tiếng Việt". |
| 4 | Nút "Nhập lại" | Button (Outline) | — | — | — | **Quy tắc hiển thị:**<br>- Nằm bên trái, viền nhạt, chữ đen, có icon refresh.<br><br>**Quy tắc hành động:**<br>- Tap → Reset tất cả field về giá trị mặc định, giữ nguyên Bottom Sheet. |
| 5 | Nút "Áp dụng" | Button (Primary) | — | — | — | **Quy tắc hiển thị:**<br>- Nằm bên phải, nền đỏ đậm, chữ trắng.<br><br>**Quy tắc hành động:**<br>- Tap → Đóng Bottom Sheet, tải lại danh sách kết quả với điều kiện lọc đã chọn. |

---

#### 2.3 Màn hình Chi tiết Thủ tục hành chính

**Mô tả giao diện:**
Header hiển thị tên thủ tục. Thân màn hình được chia thành 5 tab nội dung: Thông tin chung, Trình tự thực hiện, Thành phần hồ sơ, Cách thức thực hiện, Căn cứ pháp lý.

**Khung Header & Thông tin:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 1 | Nút Quay lại & Tiêu đề | Button & Label | Tên thủ tục | — | — | **Quy tắc hiển thị:**<br>- Header nền đỏ đậm, chữ trắng. Tiêu đề hiển thị tên thủ tục rút gọn. |
| 2 | Khối Tên & Mã thủ tục | Label Group | — | — | — | **Quy tắc hiển thị:**<br>- **Tên thủ tục**: Font đậm, chữ đen, căn trái.<br>- **Tag Cấp thực hiện**: Badge nền đỏ đậm, chữ trắng (VD: Trung ương).<br>- **Mã thủ tục**: Text xám (VD: TT-001-2024), có icon Copy bên cạnh.<br>**Quy tắc hành động:**<br>- Tap icon Copy → Sao chép mã thủ tục vào clipboard, hiển thị Toast "Đã sao chép". |
| 3 | Tab Bar | Tab Group | "Thông tin chung" | — | — | **Quy tắc hiển thị:**<br>- Thanh tab gồm 5 tab: **Thông tin chung**, **Trình tự thực hiện**, **Thành phần hồ sơ**, **Cách thức thực hiện**, **Căn cứ pháp lý**.<br><br>**Quy tắc hành động:**<br>- Hỗ trợ thao tác vuốt ngang (Swipe left/right) ở phần nội dung để chuyển tab.<br>- Hoặc Tap trực tiếp vào tên tab trên header để chuyển đổi nội dung bên dưới tương ứng. |

**Khung Nội dung chi tiết các Tab:**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
|---|---|---|---|---|---|---|
| 4 | **Tab Thông tin chung** - Khối Chi tiết | List Attribute | — | — | — | **Quy tắc hiển thị:** Hiển thị danh sách các trường (Label mờ, Value đậm):<br>- Tên thủ tục<br>- Mã thủ tục<br>- Cấp thực hiện<br>- Lĩnh vực<br>- Nhóm thủ tục<br>- Cơ quan thực hiện<br>- Đối tượng thực hiện<br>- Kết quả thực hiện<br>- Số bộ hồ sơ<br>- Tên mẫu đơn<br>- Yêu cầu & điều kiện |
| 5 | **Tab Thông tin chung** - Khối Tổng quan | List Attribute | — | — | — | **Quy tắc hiển thị:** Hiển thị 2 trường cốt lõi:<br>- Cơ quan (VD: Bộ Kế hoạch và Đầu tư)<br>- Thời hạn (VD: 15 ngày làm việc) |
| 6 | **Tab Thông tin chung** - Khối Hỗ trợ | Button Group | — | — | — | **Quy tắc hiển thị:** Gồm 2 nút: **Hotline** (có icon điện thoại), **FAQ** (có icon chấm hỏi).<br>**Quy tắc hành động:**<br>- Hotline: Tap → Hệ thống đẩy số điện thoại ra màn hình gọi (dialer) của thiết bị, không tự động thực hiện cuộc gọi luôn.<br>- FAQ: Chuyển đến màn hình Câu hỏi thường gặp. |
| 7 | **Tab Trình tự thực hiện** - Nội dung | Box Text | — | — | — | **Quy tắc hiển thị:**<br>- Hiển thị dạng văn bản hướng dẫn chi tiết các bước thực hiện. (Dữ liệu HTML hoặc text thô từ API). |
| 8 | **Tab Thành phần hồ sơ** - Danh sách | List Card | — | — | — | **Quy tắc hiển thị:** Mỗi card tương ứng 1 loại giấy tờ. Hiển thị:<br>- Tên giấy tờ/tài liệu.<br>- Tag số lượng **Bản chính**: Nền xanh dương nhạt (VD: Bản chính: 1).<br>- Tag số lượng **Bản sao**: Nền xanh lá nhạt (VD: Bản sao: 19).<br>- Nút **Tải mẫu đơn** (nếu có): Chữ đỏ, icon download.<br>**Quy tắc hành động:**<br>- Tap "Tải mẫu đơn" → Tải file thẳng về bộ nhớ của thiết bị di động (theo chuẩn tải xuống file của CMR-08). |
| 9 | **Tab Cách thức thực hiện** - Danh sách | Accordion List | — | — | — | **Quy tắc hiển thị:** Mỗi item dạng accordion:<br>- Tiêu đề: Tên hình thức (Nộp trực tiếp, Qua bưu chính...).<br>- Mở rộng hiển thị chi tiết:<br>  + **Thời hạn giải quyết**: (VD: 15 ngày làm việc).<br>  + **Phí, lệ phí**: Tag (VD: "Miễn phí" nền xanh lá).<br>  + **Mô tả chi tiết**: Đoạn văn bản mô tả nơi nộp, địa chỉ, thời gian làm việc. |
| 10 | **Tab Căn cứ pháp lý** - Danh sách | Accordion List | — | — | — | **Quy tắc hiển thị:** Mỗi item dạng accordion:<br>- Tiêu đề: Số hiệu văn bản (VD: Số 61/2020/QH14).<br>- Mở rộng hiển thị chi tiết:<br>  + Ngày ban hành & Cơ quan ban hành (VD: 17/06/2020 • Bộ Tài Chính).<br>  + Trích yếu nội dung: Tên/Mô tả luật. |

---

### 3. Mô tả các xử lý của chức năng

#### 3.1 Luồng xem danh sách và tìm kiếm
1. Người dùng truy cập chức năng "Thủ tục hành chính". Hệ thống gọi API lấy danh sách thủ tục mới nhất.
2. Khi người dùng gõ từ khóa, hệ thống áp dụng debounce 3 giây (CMR-01): sau 3 giây không gõ thêm, kết quả trả về lọc theo tên hoặc mã thủ tục.
3. Cuộn xuống để xem thêm (lazy load 20 item mỗi lần). **Lưu ý:** Khi tải thêm trang (lazy load) bị lỗi mạng hoặc timeout, hệ thống tự động **retry 3 lần** (cách nhau ~2s). Quá 3 lần vẫn lỗi mới hiển thị thông báo lỗi ở cuối danh sách (theo chuẩn CMR-04).
4. Khi nhấn nút Lọc, Bottom Sheet mở lên. Bấm "Áp dụng" để áp dụng bộ lọc Lĩnh vực, Ngôn ngữ cùng với ô tìm kiếm. Tap ra ngoài hoặc tap Đóng để thoát không áp dụng.
5. Hỗ trợ Pull to Refresh (CMR-13) để tải lại danh sách.
6. State Persistence (CMR-01): Sau khi vào chi tiết và quay lại, danh sách giữ nguyên trạng thái tìm kiếm/lọc/vị trí scroll trước đó.

#### 3.2 Luồng xem chi tiết và tải tài liệu
1. Tap vào 1 thẻ trong danh sách → Mở màn hình Chi tiết thủ tục (debounce rapid tap: chỉ nhận action đầu tiên, tránh navigate 2 lần - CMR-18).
2. Hệ thống gọi API chi tiết dựa trên mã ID thủ tục. Mọi trường thông tin nếu bị NULL sẽ tự động đổi sang ký tự "-".
3. Trong lúc chờ phản hồi, hệ thống hiển thị Skeleton loading.
4. **Partial API failure:** Nếu 1 trong nhiều API call thất bại (VD: API thành phần hồ sơ lỗi nhưng API thông tin chung thành công) → Hệ thống xử lý độc lập từng block. Block lỗi hiển thị thông báo lỗi riêng (CMR-07), các block khác hiển thị bình thường.
5. Thông tin hiển thị chia thành 5 Tab, người dùng có thể **vuốt ngang (swipe left/right)** hoặc nhấn trực tiếp vào tab để chuyển.
6. Tại tab **Thành phần hồ sơ**, người dùng có thể tải thẳng các biểu mẫu đính kèm (nếu có) về máy. Tại header, nhấn icon Copy để chép mã thủ tục.

#### 3.3 Xử lý session
- **Session expire:** Xử lý session được quy định tại UC1 (Trang chủ Dashboard).
- **Force close (tắt app không xóa dữ liệu):** Khi người dùng mở lại app, hệ thống quay về Trang chủ.
- **Xóa app (uninstall):** Yêu cầu đăng nhập lại từ đầu (đối với cá nhân/tổ chức có tài khoản). Chức năng này public nên nếu không đăng nhập vẫn sử dụng bình thường.

#### 3.4 Xử lý lỗi (Tham chiếu CMR-07)

| Tình huống lỗi | Thông báo hiển thị | Hành vi hệ thống |
| --- | --- | --- |
| Lỗi kết nối mạng | *"Không thể kết nối. Vui lòng kiểm tra mạng và thử lại."* | Giữ nguyên màn hình, hiển thị nút **"Thử lại"**. |
| Không tìm thấy kết quả | *"Không tìm thấy kết quả."* | Hiển thị empty state theo chuẩn CMR-14, ẩn danh sách kết quả. |
| Lỗi tải file đính kèm | *"Nội dung không tồn tại hoặc đã bị xóa."* | Khi bấm tải biểu mẫu nhưng file bị lỗi trên server, hiển thị Toast lỗi. |

#### 3.5 Tiêu chí chấp nhận (Acceptance Criteria)
- **AC1:** Tìm kiếm realtime theo Tên thủ tục/mã thủ tục, debounce 3 giây hoạt động đúng (CMR-01).
- **AC2:** Bottom Sheet bộ lọc (Lĩnh vực, Ngôn ngữ) kết hợp với ô tìm kiếm khi bấm "Áp dụng". Nút "Nhập lại" reset về mặc định. Icon Lọc hiển thị chấm xanh (indicator) khi đang lọc.
- **AC3:** Màn hình danh sách hiển thị đúng giao diện card. Hỗ trợ Lazy load 20 item (tự retry 3 lần khi lỗi mạng) và Pull to Refresh.
- **AC4:** Màn hình chi tiết hiển thị đầy đủ 5 tab, hỗ trợ thao tác vuốt ngang (Swipe left/right) để chuyển tab trơn tru.
- **AC5:** Ở tab Thành phần hồ sơ, tag số lượng bản chính/bản sao hiển thị đúng. Biểu mẫu đính kèm (nếu có) tải trực tiếp về bộ nhớ máy thành công khi tap.
- **AC6:** Nút Copy ở header màn hình chi tiết sao chép đúng mã thủ tục và hiện toast xác nhận. Nút Hotline mở trình gọi điện (dialer) với số có sẵn.
- **AC7:** State Persistence (CMR-01): Trở về từ màn hình chi tiết, danh sách giữ nguyên trạng thái tìm kiếm, lọc và scroll.
- **AC8:** Partial API failure: Nếu 1 API block thất bại, các block khác vẫn hiển thị bình thường, block lỗi hiển thị thông báo lỗi riêng.

#### 3.6 Đa ngôn ngữ (→ Xem CMR-17)
Toàn bộ text cứng trên màn hình (header, placeholder ô tìm kiếm, label dropdown, tên các tab, thông báo lỗi, empty state message, toast) được dịch sang ngôn ngữ hiển thị tương ứng (VI, EN, ZH, JA, KO). Nội dung dữ liệu từ API (tên thủ tục, chi tiết HTML) hiển thị nguyên bản hoặc trả về theo ngôn ngữ nếu API hỗ trợ.

---

### 4. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 12/05/2026 | v1.0 | Tạo mới | (Không có) | Tạo mới tài liệu SRS | Dựa trên luồng UC69 và cấu trúc cũ |
| 12/05/2026 | v2.0 | Cập nhật theo UI Design mới | Cấu trúc tab chung chung | Chuẩn hóa UI 5 tab: Thông tin chung, Thành phần hồ sơ, Cách thức thực hiện, Căn cứ pháp lý. Thêm nút Copy. | Theo design bộ ảnh mới update |
| 12/05/2026 | v3.0 | Cập nhật chuẩn Form UC69 | Format bảng và cấu trúc tự do | Cập nhật cấu trúc bảng 7 cột, chia các section 3.2, 3.3 giống hệt UC69 | Đồng bộ toàn diện với chuẩn Form UC69 |
| 12/05/2026 | v4.0 | Làm rõ các case (Audit Feedback) | Thiếu chi tiết thao tác | Cập nhật: indicator bộ lọc, swipe tab ngang, push số ra dialer, retry lazy load 3 lần, tải file trực tiếp. | Theo Q&A Audit ngày 12/05 |
