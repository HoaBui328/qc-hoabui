# ĐẶC TẢ YÊU CẦU NGƯỜI SỬ DỤNG

**Tiêu đề:** UC54 — Tra cứu báo cáo nhà đầu tư đã nộp cho cơ quan Nhà nước trên Mobile
**Ngày tạo:** 29/04/2026
**Phiên bản:** v2.11

| Thuộc tính              | Giá trị                                 |
| ------------------------- | ----------------------------------------- |
| BA phụ trách            | han.luong & huy.lai2                      |
| Phân hệ                 | Ứng dụng Di động (Mobile App)         |
| Loại chức năng         | Tra cứu báo cáo                        |
| Đối tượng thực hiện | Cá nhân / Tổ chức (đã đăng nhập) |
| Giao diện                | Màn hình Mobile (Portrait)              |
| Ngày tạo                | 29/04/2026                                |
| Phiên bản               | v2.11                                     |

---

## UC54 — Tra cứu báo cáo nhà đầu tư đã nộp cho cơ quan Nhà nước trên Mobile

### 1. Mô tả chức năng

**Tên chức năng:** Tra cứu báo cáo nhà đầu tư đã nộp cho cơ quan Nhà nước trên Mobile
**Mô tả:** Chức năng cho phép cá nhân, tổ chức xem danh sách các báo cáo đã nộp cho cơ quan Nhà nước thông qua hệ thống và tra cứu theo tiêu chí lọc. Hệ thống hiển thị báo cáo được phân loại theo các tab trạng thái.
**Phân quyền:** Cá nhân/Tổ chức đã đăng nhập chỉ xem được báo cáo của chính mình nộp.
**Lưu ý:** Giao diện, dữ liệu hiển thị, và các tùy chọn filter của **Cá nhân** và **Tổ chức là giống nhau**, không có khác biệt về hành vi hay UI.
**Truy cập chức năng:** Sidebar → "Báo cáo đã nộp".
**Chức năng đáp ứng usecase số:** UC54 (Phụ lục XIV — Nhóm C.V)

**Hậu điều kiện (Postcondition):** Hành động tra cứu/xem danh sách không làm thay đổi trạng thái dữ liệu của hệ thống và không yêu cầu ghi nhận audit log.

**Quy tắc đồng bộ dữ liệu:**

- Dữ liệu báo cáo trên UC54 (Mobile) được **đồng bộ real-time** với phân hệ Báo cáo trên Web.
- Khi nhà đầu tư nộp báo cáo trên Web → Dữ liệu cập nhật ngay trên Mobile mà không cần thao tác làm mới (pull-to-refresh).
- Khi trạng thái báo cáo thay đổi trên Web (ví dụ: Đã duyệt, Yêu cầu bổ sung, Từ chối) → Stat Banner và danh sách trên Mobile tự động cập nhật theo.
- Tương tự, các thao tác trên Mobile (nếu có) cũng phản ánh ngay lên phân hệ Web.
- **Khi mất kết nối mạng:** Giữ nguyên dữ liệu cũ trên màn hình hiện tại và hiển thị thông báo lỗi mạng. (Xem CMR-07)
- **Khi mất kết nối giữa chừng (đã load một phần danh sách qua lazy load):** Giữ nguyên toàn bộ dữ liệu đã load, không xóa các bản ghi đã hiển thị. Chỉ hiển thị thông báo lỗi mạng khi người dùng cuộn đến cuối danh sách và hệ thống không thể tải trang tiếp theo. (Xem CMR-07)
- **Khi khôi phục kết nối:** Hiển thị thông báo khôi phục kết nối. Người dùng có thể **pull-to-refresh** để đồng bộ lại dữ liệu mới nhất. (Xem CMR-13)

---

### 2. Mô tả giao diện

#### 2.1 Giao diện Danh sách báo cáo đã nộp

**Mô tả giao diện:**
Màn hình cuộn dọc bắt đầu bằng Header đỏ đặc trưng. Bên dưới Header là thanh chỉ số trạng thái (Stat Banner) cuộn ngang, tiếp đến là thanh tìm kiếm kết hợp bộ lọc, và cuối cùng là danh sách Card báo cáo hiển thị chi tiết thông tin dự án và trạng thái.

**Khả năng truy cập (Accessibility — riêng UC-54):**
- **Minimum Touch Target (48x48dp):** Áp dụng bắt buộc cho: Icon mở Modal bộ lọc, Nút xóa Text (X) trong ô tìm kiếm, và Icon/Nút tải xuống trên mỗi Card báo cáo để tránh user thao tác nhầm khi lướt danh sách.
- **Screen Reader:** Các icon không có text (như Download) phải được bổ sung content description/alt-text. Khi focus vào 1 Card, hệ thống đọc tuần tự: "Tên báo cáo" → "Trạng thái" → "Ngày nộp".
- **Font Scaling:** Khu vực Stat Banner và Card List hỗ trợ wrap-text linh hoạt, không vỡ layout khi người dùng tăng cỡ chữ hệ thống.
- **Contrast Ratio:** Các thẻ màu trạng thái (Badge Vàng, Xanh lá, Cam theo CMR-05) đảm bảo tỷ lệ tương phản tối thiểu 4.5:1 giữa chữ và nền.

**Khung Header:**

| # | Tên trường       | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú                                                                       |
| - | ------------------- | -------------- | --------------------- | ------------ | ---------- | -------------------------------------------------------------------------------------- |
| 1 | Nút Quay lại (←) | Button (Icon)  | —                    | —           | —         | **Quy tắc hành động:** Tap → Quay về màn hình trước đó. (Xem CMR-06) |
| 2 | Tiêu đề Header   | Label          | "Báo cáo đã nộp" | —           | —         | **Quy tắc hiển thị:** Màu trắng trên nền đỏ đậm, căn giữa.          |

**Quy tắc chung cho Search/Filter & State Persistence:**

- Khi người dùng chuyển sang **mục khác trên Sidebar (Left Sidebar)** và quay lại → **Reset** search/filter về mặc định.

**Thanh chỉ số trạng thái (Stat Banner):**

> Thanh này hiển thị tổng quan số lượng báo cáo theo từng trạng thái, hỗ trợ cuộn ngang (Horizontal Scroll).

**Quy tắc hành động:** Các thẻ chỉ số trạng thái là **read-only, không thể tap (unclickable)**. Thẻ **luôn hiển thị tổng số lượng toàn bộ** — không thay đổi khi Filter/Search đang active. Thẻ chỉ hiển thị thông tin tổng quan, không trigger filter danh sách.

**Quy tắc hiển thị số lượng:**

- Số lượng báo cáo trên mỗi thẻ được **hệ thống tự động đếm (count)** từ API theo từng trạng thái tương ứng.
- **Quy tắc format số:**
  - Phân cách hàng nghìn bằng dấu phẩy `,` (VD: 1,235).
  - Hiển thị tối đa 3 chữ số thập phân; tự động cắt bỏ các số 0 vô nghĩa ở cuối (VD: 123.320 → 123.32).
  - Nếu giá trị < 0.001 → Hiển thị "< 0.001".
  - (Xem CMR-11)

| # | Tên chỉ số       | Kiểu hiển thị    | Mô tả/Ghi chú                                                                                                                       |
| - | ------------------- | ------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Tổng số báo cáo | Card (Icon + Label) | Nền trắng, icon xanh dương. Hiển thị tổng số lượng báo cáo.**(Hệ thống tự count theo trạng thái)** (Xem CMR-11) |
| 2 | Lưu nháp         | Card (Icon + Label) | Nền xám nhạt, icon file xám. Số lượng được hệ thống tự count. (Xem CMR-11)                                              |
| 3 | Chờ duyệt        | Card (Icon + Label) | Nền vàng nhạt, icon đồng hồ vàng. Số lượng được hệ thống tự count. (Xem CMR-11)                                        |
| 4 | Đã tiếp nhận     | Card (Icon + Label) | Nền xanh dương nhạt, icon tích xanh. Số lượng được hệ thống tự count. (Xem CMR-11)                                     |
| 5 | Yêu cầu chỉnh sửa | Card (Icon + Label) | Nền cam nhạt, icon chấm than cam. Số lượng được hệ thống tự count. (Xem CMR-11)                                            |

**Khung Tìm kiếm & Lọc:**

| # | Tên trường | Kiểu trường       | Giá trị mặc định              | Được sửa | Bắt buộc | Mô tả/Ghi chú                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | ------------- | -------------------- | ---------------------------------- | ------------ | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Ô tìm kiếm | Textbox (Search)     | "Tìm kiếm nhanh theo tên dự án" | x            | —         | **Quy tắc hiển thị:** (Xem CMR-01)<br>- Icon kính lúp nằm bên trái trong ô.<br>- Tìm kiếm gần đúng (like) theo tên dự án — tìm kiếm chứa từ khóa, không yêu cầu nhập chính xác toàn bộ tên. Khi xóa hết từ khóa, danh sách trở về trạng thái mặc định.<br>- Max length: **255 ký tự**. Khi nhập đủ 255 ký tự, không cho phép nhập thêm.<br><br>**Quy tắc hành động:** (Xem CMR-01)<br>- Nhập từ khóa → Kết quả hiển thị tự động sau **3 giây debounce**. Người dùng nhập từ khóa → Kết quả hiển thị ngay, không cần nhấn Enter hay nhấn nút nào.<br>- Tự động trim space (cắt khoảng trắng hai đầu) trước khi tìm kiếm. Nếu sau trim rỗng → không trigger search, danh sách về mặc định.<br>- Nếu không có kết quả trùng khớp: Hiển thị màn *"Không tìm thấy kết quả."* (Xem CMR-14) |
| 2 | Nút "Lọc"   | Button (Icon Filter) | —                                 | —           | —         | **Quy tắc hiển thị:**<br>- Nằm bên phải ô tìm kiếm, viền bo tròn, icon bộ lọc.<br>- Khi có filter đang active (giá trị khác mặc định) → Hiển thị **icon indicator màu xanh lá cây** ở góc phải bên trên của icon filter. Khi không có filter active → ẩn indicator. (Xem CMR-02)<br><br>**Quy tắc hành động:** (Xem CMR-02)<br>- Tap icon filter → Mở modal/panel bộ lọc.<br>- Tap 'Áp dụng' / 'Tìm' → Đóng bộ lọc, tải lại danh sách với tiêu chí đã chọn.<br>- Tap 'Nhập lại' / 'Đặt lại' → Reset tất cả trường về giá trị mặc định.<br>- Tap vùng ngoài hoặc nút 'X' → Đóng bộ lọc, không thay đổi kết quả hiện tại.                                                                                                                         |

**Modal Bộ lọc tìm kiếm (Bottom Sheet):**

> Bộ lọc hiển thị dưới dạng Bottom Sheet. Người dùng chỉnh sửa các tiêu chí trong sheet, sau đó tap "Áp dụng" để áp dụng. Bottom Sheet có nút "X" ở góc phải trên cùng để đóng.

| # | Tên trường     | Kiểu trường              | Giá trị mặc định        | Được sửa | Bắt buộc | Mô tả/Ghi chú                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - | ----------------- | --------------------------- | ---------------------------- | ------------ | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Loại báo cáo      | Dropdown (Single-selection) | "Tất cả"    | x            | —         | **Quy tắc hiển thị:** (Xem CMR-03)`<br>`- Danh sách loại báo cáo lấy từ Master Data của hệ thống (Ví dụ: Báo cáo tiến độ dự án, Báo cáo kết quả kinh doanh, Báo cáo nhân sự...).`<br>`- Giá trị mặc định: "Tất cả".`<br><br>`**Quy tắc hành động:** (Xem CMR-03)`<br>`- Người dùng có thể tìm kiếm/filter trong dropdown (tìm kiếm gần đúng).`<br>`- Xóa hết keyword → hiển thị lại placeholder trong ô search của dropdown (CMR-03).`<br>`- Tap ra ngoài khi keyword trống → tự động chọn lại "Tất cả" (CMR-03).`<br>`- Nếu không khớp → hiển thị "Không có dữ liệu." (Xem CMR-03). |
| 2 | Trạng thái      | Dropdown (Single-selection) | "Tất cả" | x            | —         | **Quy tắc hiển thị:** (Xem CMR-03)`<br>`- Danh sách trạng thái lấy từ danh mục hệ thống (Lưu nháp, Chờ duyệt, Đã tiếp nhận, Yêu cầu chỉnh sửa).`<br>`- Giá trị mặc định: "Tất cả".`<br><br>`**Quy tắc hành động:** (Xem CMR-03)`<br>`- Người dùng có thể tìm kiếm/filter trong dropdown (tìm kiếm gần đúng).`<br>`- Xóa hết keyword → hiển thị lại placeholder trong ô search của dropdown (CMR-03).`<br>`- Tap ra ngoài khi keyword trống → tự động chọn lại "Tất cả" (CMR-03).`<br>`- Nếu không khớp → hiển thị "Không có dữ liệu." (Xem CMR-03). |
| 3 | Tỉnh/thành phố    | Dropdown (Single-selection) | "Tất cả"  | x            | —         | **Quy tắc hiển thị:** (Xem CMR-03)`<br>`- Danh sách lấy từ danh mục Tỉnh/Thành phố của hệ thống.`<br>`- Giá trị mặc định: "Tất cả".`<br><br>`**Quy tắc hành động:** (Xem CMR-03)`<br>`- Người dùng có thể tìm kiếm/filter trong dropdown (tìm kiếm gần đúng).`<br>`- Xóa hết keyword → hiển thị lại placeholder trong ô search của dropdown (CMR-03).`<br>`- Tap ra ngoài khi keyword trống → tự động chọn lại "Tất cả" (CMR-03).`<br>`- Nếu không khớp → hiển thị "Không có dữ liệu." (Xem CMR-03). |
| 4 | Nút "X" đóng   | Button (Icon)               | —                           | —           | —         | **Quy tắc hiển thị:** Icon "X" nằm ở góc trên phải của Bottom Sheet. Màu xám đậm, viền bo tròn nếu có nền.`<br><br>`**Quy tắc hành động:**`<br>`- Tap vùng ngoài hoặc tap nút "X" → Đóng Bottom Sheet, không thay đổi kết quả hiện tại.`<br>`- Nhấn nút Back vật lý (Android) khi Bottom Sheet đang mở → Đóng Bottom Sheet (không thoát màn hình). (Xem CMR-02)                                                                                                                                                                                                                                                                                                                                                               |
| 5 | Nút "Nhập lại" | Button (Secondary)          | —                           | —           | —         | **Quy tắc hiển thị:** Nút viền outline màu đỏ, text màu đỏ. Không đóng Bottom Sheet.`<br><br>`**Quy tắc hành động:** (Xem CMR-02)`<br>`- Tap → Reset toàn bộ tiêu chí lọc về giá trị mặc định.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 6 | Nút "Áp dụng"  | Button (Primary)            | —                           | —           | —         | **Quy tắc hiển thị:** Nút nền đỏ filled, text trắng.`<br><br>`**Quy tắc hành động:** (Xem CMR-02)`<br>`- Tap → Áp dụng toàn bộ tiêu chí lọc hiện tại.`<br>`- Đóng Bottom Sheet.`<br>`- Gọi API với tham số bộ lọc và tải lại danh sách báo cáo.`<br>`- Nếu không có kết quả phù hợp → hiển thị "Không tìm thấy kết quả." (Xem CMR-14)                                                                                                                                                                                                                                                 |

**Khung Danh sách báo cáo (Card List):**

> Mỗi card đại diện cho một báo cáo. Danh sách sắp xếp mặc định theo **ngày tạo** giảm dần (mới nhất lên đầu).

**Debounce navigation & Khôi phục trạng thái:** (Xem CMR-18)

- **Debounce navigation:** Khi người dùng tap nhanh liên tục (double tap) vào các button navigation (Quick Access cards, Footer tabs, Sidebar items), hệ thống có cơ chế debounce.
- **Force close** (tắt app không xóa dữ liệu): Khi người dùng mở lại app sau khi force close, hệ thống quay về **Trang chủ** và **giữ nguyên session đăng nhập**, không yêu cầu đăng nhập lại.
- **Xóa app** (uninstall): Khi người dùng xóa app và cài đặt lại, hệ thống **yêu cầu đăng nhập lại từ đầu** (không restore session).

**Đa ngôn ngữ (CMR-17):** Hỗ trợ 5 ngôn ngữ (VI, EN, ZH, JA, KO). Text cứng của ứng dụng (header, tên field/label, tên tab, tên nút, placeholder, thông báo lỗi, empty state message) thay đổi theo ngôn ngữ đã chọn. Nội dung dữ liệu từ API (tên báo cáo, trạng thái, ghi chú) hiển thị nguyên bản, không thay đổi theo ngôn ngữ.

| # | Tên trường           | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú                                                                                                                                                                                                                     |
| - | ----------------------- | -------------- | --------------------- | ------------ | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1 | Tên dự án            | Label (Bold)   | —                    | —           | —         | **Quy tắc hiển thị:** Màu đen đậm. Hiển thị tối đa 2 dòng, quá dài sẽ truncate với "..." ở cuối.<br>- Nếu null → **ẩn toàn bộ field** (không hiển thị dòng này trên card). |
| 2 | Mã báo cáo           | Label (Bold)   | —                    | —           | —         | **Quy tắc hiển thị:** Màu đỏ đậm (ví dụ: "BC-2026-001"). Hiển thị tối đa 1 dòng, quá dài sẽ truncate với "..." ở cuối.                                                                                    |
| 3 | Trạng thái            | Badge          | —                    | —           | —         | **Quy tắc hiển thị:** (Xem CMR-05)<br><br>**Bảng mapping màu sắc:**<br>- Lưu nháp → Xám<br>- Chờ duyệt → Vàng<br>- Đã tiếp nhận → Xanh lá<br>- Yêu cầu chỉnh sửa → Cam<br><br>**Quy tắc hành động:** Badge trạng thái luôn read-only, không cho phép tap.                                    |
| 4 | Tên báo cáo           | Label          | —                    | —           | —         | **Quy tắc hiển thị:** Text thường màu đen (Ví dụ: "Báo cáo tiến độ dự án"). Hiển thị tối đa 2 dòng, quá dài sẽ truncate với "..." ở cuối.                                                                                    |
| 5 | Cơ quan tiếp nhận    | Label          | —                    | —           | —         | **Quy tắc hiển thị:** Tiền tố "Cơ quan tiếp nhận: " + Tên cơ quan. Text thường màu đen. Hiển thị tối đa 2 dòng, quá dài sẽ truncate với "..." ở cuối.<br>- Nếu null → **ẩn toàn bộ field** (không hiển thị dòng này trên card). |
| 6 | Metadata              | Label          | —                    | —           | —         | **Quy tắc hiển thị:** Hiển thị linh hoạt theo dữ liệu có sẵn:<br>- Có cả 2 → "Kỳ: [Giá trị] • Ngày cập nhật: [DD/MM/YYYY]" (Xem CMR-12)<br>- Chỉ có Kỳ → "Kỳ: [Giá trị]"<br>- Chỉ có Ngày cập nhật → "Ngày cập nhật: [DD/MM/YYYY]"<br>- Cả 2 null → **ẩn toàn bộ field** (không hiển thị dòng này trên card). |
| 7 | Nút "Download"          | Button (Icon)  | —                    | —           | —         | **Quy tắc hiển thị:** Icon Download nằm trong Card báo cáo.<br><br>**Quy tắc hành động:** Tap → Tải tệp báo cáo đính kèm (theo định dạng quy định, ví dụ PDF/Doc). (Xem CMR-08)<br><br>**UI Feedback:** Khi tap → Icon download chuyển sang trạng thái loading spinner cục bộ. Khi hoàn thành → Hiển thị Toast: *"Tải tệp thành công"* hoặc *"Tải tệp thất bại. Vui lòng thử lại"*. |

---

### 3. Mô tả các xử lý của chức năng

#### 3.1 Xử lý Tải danh sách báo cáo

1. Người dùng truy cập màn hình Báo cáo đã nộp.
2. Hệ thống gọi API lấy danh sách báo cáo của người dùng hiện tại.
3. Danh sách sắp xếp theo **ngày tạo** giảm dần (Mới nhất lên đầu).
4. **Lazy load:** Tải 20 bản ghi/lần. Khi cuộn đến cuối, tự động tải trang tiếp theo. (Xem CMR-04)

**Pull to refresh:** (Xem CMR-13)

- Kéo xuống từ đầu danh sách → Trigger refresh dữ liệu từ đầu.
- Hiển thị spinner ở đầu danh sách trong khi đang refresh.
- Sau khi refresh thành công: Cập nhật danh sách, ẩn spinner.

**Xử lý lỗi cục bộ (Section-level error isolation):**

- Nếu **API Stat Banner lỗi** & API List thành công: Khu vực Banner hiển thị giá trị "-" (hoặc ẩn), danh sách Card List bên dưới vẫn hiển thị bình thường để user tiếp tục làm việc.
- Nếu **API List lỗi** & API Banner thành công: Banner vẫn hiện số liệu, khu vực danh sách hiển thị Empty State báo lỗi *"Không thể tải dữ liệu. Vui lòng thử lại."* kèm nút **"Thử lại"**. (Xem CMR-07)

**Xử lý lỗi toàn màn hình:** (Xem CMR-07, 16)

**Loading state:** (Xem CMR-07) First-load (lần đầu vào màn hình): Hiển thị loading state toàn màn hình (full-screen loading overlay). Các lần tải tiếp theo (lazy load, refresh): Sử dụng loading indicator cục bộ (spinner).

**Lazy load retry:** (Xem CMR-04) Khi tải trang N bị lỗi → Hệ thống tự động retry 3 lần (mỗi lần cách nhau ~2 giây). Sau 3 lần retry vẫn fail → Dừng tự động retry, hiển thị thông báo lỗi cục bộ ở cuối danh sách. Người dùng có thể dùng pull-to-refresh để tải lại từ đầu.

| Tình huống lỗi            | Thông báo hiển thị                                                                             | Hành vi hệ thống                                                                                                                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Lỗi mạng / Mất kết nối  | *"Không thể kết nối. Vui lòng kiểm tra mạng và thử lại."* + nút **"Thử lại"** | Giữ nguyên màn hình, hiển thị nút Thử lại.                                                                                                                                                               |
| Lỗi API (HTTP 500)          | *"Hệ thống đang bận. Vui lòng thử lại sau."*                                              | Giữ nguyên màn hình, chỉ hiển thị thông báo.                                                                                                                                                             |
| Timeout (>10 giây)          | *"Yêu cầu đã hết thời gian chờ. Vui lòng thử lại."* + nút **"Thử lại"**       | Giữ nguyên màn hình, hiển thị nút Thử lại. (Xem CMR-16)                                                                                                                                                  |
| Session hết hạn (HTTP 401) | Toast:*"Phiên đăng nhập hết hạn."*                                                         | Hệ thống tự động sử dụng refresh token để cấp lại access token mới. Nếu refresh token hết hạn hoặc không hợp lệ (quá**15 ngày**) → Redirect về màn hình đăng nhập. (Xem CMR-07) |

**Xử lý lỗi trống (Empty state):** (Xem CMR-14)

- **Trường hợp 1 — Hệ thống rỗng:** Khi user mở màn hình lần đầu (chưa thực hiện search/filter), hệ thống ghi nhận tài khoản chưa nộp báo cáo nào → Hiển thị: *"Không có dữ liệu."*
- **Trường hợp 2 — Tìm kiếm rỗng:** Khi hệ thống đã có dữ liệu nhưng kết quả Search/Filter trả về mảng rỗng → Hiển thị: *"Không tìm thấy kết quả."*

#### 3.2 Tiêu chí chấp nhận (Acceptance Criteria)

- **AC1:** Thanh Stat Banner hiển thị đúng 5 chỉ số trạng thái (Tổng số, Lưu nháp, Chờ duyệt, Đã tiếp nhận, Yêu cầu chỉnh sửa) với số lượng tự count và format theo CMR-11. Count không thay đổi khi Filter/Search đang active.
- **AC2:** Card báo cáo hiển thị đầy đủ theo thứ tự: Tên dự án (đen đậm, tối đa 2 dòng), Mã báo cáo (đỏ đậm), Badge trạng thái (màu đúng theo mapping), Tên báo cáo (text thường), Cơ quan tiếp nhận, Metadata (Kỳ • Ngày cập nhật), Nút Download. Các field có logic ẩn khi null (Tên dự án, Cơ quan tiếp nhận, Metadata) phải ẩn đúng khi dữ liệu không có.
- **AC3:** Nút Download hiển thị loading spinner cục bộ khi tap, và Toast kết quả (thành công/thất bại) sau khi hoàn thành.
- **AC4:** Empty State hiển thị đúng message theo ngữ cảnh: "Không có dữ liệu." (hệ thống rỗng) / "Không tìm thấy kết quả." (search/filter rỗng).

---

## 4. Lịch sử cập nhật

| Ngày      | Phiên bản  | Mục cập nhật                                       | Before                                                                                           | After                                                                                                                                                                                | Ghi chú                                          |
| ---------- | ------------ | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------- |
| 2026-05-08 | v2 → v2.1   | §3.1 — Xử lý Tải danh sách báo cáo (bước 2) | "Hệ thống mặc định lọc theo Năm hiện tại và gọi API lấy danh sách."                 | "Hệ thống gọi API lấy danh sách báo cáo của người dùng hiện tại."                                                                                                       | Không có filter năm trong UC54                 |
| 2026-05-08 | v2 → v2.1   | §3.2 — AC5 (Nút Download)                          | "AC5: Nút Download tải được tệp báo cáo đính kèm đúng theo CMR-08."                 | (Đã xóa)                                                                                                                                                                          | Không có nút Download trong UC54               |
| 2026-05-08 | v2 → v2.1   | §2.1 — Quy tắc Search/Filter State Persistence     | "Khi người dùng chuyển sang tab khác và quay lại → Reset search/filter về mặc định." | "Khi người dùng chuyển sang mục khác trên Sidebar (Left Sidebar) và quay lại → Reset search/filter về mặc định."                                                       | UC54 không có tab; truy cập từ Sidebar        |
| 2026-05-08 | v2 → v2.1   | §1 — Quy tắc đồng bộ dữ liệu                  | Chỉ mô tả happy-path real-time sync                                                           | Thêm 2 rule fallback: mất kết nối → giữ dữ liệu cũ + thông báo lỗi mạng (CMR-07); khôi phục → thông báo + pull-to-refresh (CMR-13)                                 | Bổ sung xử lý offline/reconnect                |
| 2026-05-08 | v2 → v2.1   | §2.1 — Stat Banner: Quy tắc format số             | 3 bullet inline mô tả K/M format (1,234; 2.3M; 1.5K…)                                         | Thay bằng "Quy tắc format số: Xem CMR-11"                                                                                                                                         | Delegate chi tiết format cho CMR-11              |
| 2026-05-08 | v2 → v2.1   | §2.1 — Stat Banner: Hành vi tap                    | (Không có)                                                                                     | "Các thẻ chỉ số trạng thái là read-only, không thể tap (unclickable). Thẻ chỉ hiển thị thông tin tổng quan, không trigger filter danh sách."                        | Làm rõ Stat Banner unclickable                  |
| 2026-05-08 | v2 → v2.1   | §2.2 — Quy tắc đóng/mở section chi tiết        | (Không có)                                                                                     | "Các section 2.2.3 → 2.2.9 có thể đóng/mở (collapsible). Mặc định: tất cả section ở trạng thái mở. Đóng/mở section này không ảnh hưởng section khác."       | Thêm rule collapsible + trạng thái mặc định |
| 2026-05-08 | v2 → v2.1   | §2.1 — Card List: Debounce tap                      | (Không có)                                                                                     | "Debounce tap: tap nhanh nhiều lần trên cùng một card → chỉ trigger 1 lần navigation (debounce 500ms)."                                                                      | Tránh mở nhiều màn hình trùng lặp          |
| 2026-05-07 | v2.1 → v2.2 | §2.1 — Debounce & Khôi phục trạng thái          | Chỉ có debounce tap 500ms                                                                      | Cập nhật debounce navigation + force close giữ session + uninstall yêu cầu đăng nhập lại (CMR-18)                                                                           | Mở rộng rule                                    |
| 2026-05-07 | v2.1 → v2.2 | §2.2.1 — Xóa field "Ngày nộp"                    | Field #4 "Ngày nộp" (Icon lịch + DD/MM/YYYY HH:mm)                                            | (Đã xóa)                                                                                                                                                                          | Bỏ field theo yêu cầu                          |
| 2026-05-07 | v2.1 → v2.2 | Modal Lịch sử báo cáo                             | Timeline tăng dần + bảng 5 bước cố định                                                  | Mô tả gọn: bước xử lý, tên người xử lý, thời gian xử lý. Sắp xếp**giảm dần** (mới nhất trên). Xóa bảng ví dụ cứng                                   | Đơn giản hóa + sửa thứ tự sort             |
| 2026-05-08 | v2 → v2.1   | §1 — Phân quyền: Cá nhân vs Tổ chức           | "Cá nhân/Tổ chức đã đăng nhập chỉ xem được báo cáo của chính mình nộp."       | Giữ nguyên + thêm: "Giao diện, dữ liệu hiển thị, và các tùy chọn filter của Cá nhân và Tổ chức là giống nhau, không có khác biệt về hành vi hay UI."       | Làm rõ không có khác biệt CN/TC             |
| 2026-05-07 | v2.1 → v2.2 | Bảng Xử lý lỗi — Thêm HTTP 401                  | (Không có)                                                                                     | Session hết hạn (HTTP 401): tự động sử dụng refresh token; nếu refresh token hết hạn (>15 ngày) → redirect đăng nhập + toast "Phiên đăng nhập hết hạn" (CMR-07) | Bổ sung xử lý session                          |
| 2026-05-12 | v2.2 → v2.3 | Bổ sung CMR-17 (Đa ngôn ngữ) | (Không có) | Hỗ trợ 5 ngôn ngữ (VI, EN, ZH, JA, KO) cho text cứng | Đồng bộ Cross-UC Inconsistency Report v2 |
| 2026-05-13 | v2.3 → v2.4 | Cập nhật Trang chủ (Danh sách báo cáo) | - Có 6 trạng thái Stat Banner<br>- Tìm kiếm theo mã báo cáo<br>- Card hiển thị Dự án, NĐT, Vị trí, chữ "Nộp"<br>- Có filter Loại BC, Tỉnh/thành | - Có 5 trạng thái (Lưu nháp, Chờ duyệt, Đã tiếp nhận, Yêu cầu chỉnh sửa)<br>- Tìm kiếm theo tên dự án<br>- Card bỏ Dự án, NĐT, Tỉnh thành; đổi "Ngày tiếp nhận"; thêm nút Download<br>- Filter chỉ còn Trạng thái | Yêu cầu thay đổi từ Figma |
| 2026-05-13 | v2.4 → v2.5 | Xóa màn hình Chi tiết báo cáo | - Có màn hình chi tiết gồm 7 section và Modal lịch sử<br>- Có icon điều hướng trên Card List | - Xóa toàn bộ phần Giao diện Chi tiết báo cáo (2.2)<br>- Xóa Modal Lịch sử báo cáo<br>- Bỏ icon điều hướng trên card | Yêu cầu thay đổi từ Figma (Bỏ hẳn màn chi tiết) |
| 2026-05-14 | v2.5 → v2.6 | §1 — Postcondition | (Không có) | Bổ sung: "Hành động tra cứu không làm thay đổi dữ liệu, không ghi audit log" | Feedback QA/Reviewer |
| 2026-05-14 | v2.5 → v2.6 | §2.1 — Accessibility | (Không có) | Bổ sung sub-section: Touch Target 48dp, Screen Reader thứ tự đọc Card, Font Scaling wrap-text, Contrast Ratio 4.5:1 | Feedback QA/Reviewer |
| 2026-05-14 | v2.5 → v2.6 | §2.1 — Stat Banner: Count khi filter | "Thẻ chỉ hiển thị thông tin tổng quan" | Bổ sung: "Luôn hiển thị tổng số lượng toàn bộ, không thay đổi khi Filter/Search active" | Feedback QA/Reviewer |
| 2026-05-14 | v2.5 → v2.6 | §2.1 — Modal Bộ lọc: Dropdown no-result | Không đề cập | Bổ sung: Khi nhập text không khớp option nào → hiển thị inline "Không tìm thấy dữ liệu" | Feedback QA/Reviewer |
| 2026-05-14 | v2.5 → v2.6 | §2.1 — Card List: Tên dự án | (Không có — Card bắt đầu bằng Mã báo cáo) | Thêm trường Tên dự án (Bold, 2 dòng) làm field #1 trên Card | Feedback QA/Reviewer |
| 2026-05-14 | v2.5 → v2.6 | §2.1 — Card List: Badge mapping màu | "Màu sắc dựa theo UI design" | Bảng mapping cụ thể: Lưu nháp=Xám, Chờ duyệt=Vàng, Đã tiếp nhận=Xanh lá, Yêu cầu chỉnh sửa=Cam | Feedback QA/Reviewer |
| 2026-05-14 | v2.5 → v2.6 | §2.1 — Card List: Download UI Feedback | Chỉ ghi "Tap → Tải tệp" | Bổ sung: Spinner cục bộ khi tap, Toast thành công/thất bại khi hoàn thành | Feedback QA/Reviewer |
| 2026-05-14 | v2.5 → v2.6 | §3.1 — Section-level error isolation | (Không có) | Bổ sung: API Banner lỗi → Banner hiển thị "-", List vẫn OK; API List lỗi → Banner OK, List hiển thị lỗi cục bộ + Thử lại | Feedback QA/Reviewer |
| 2026-05-14 | v2.5 → v2.6 | §3.1 — Empty State: Phân biệt 2 trường hợp | 2 dòng gộp chung | Tách rõ TH1 (hệ thống rỗng → "Không có dữ liệu.") và TH2 (search/filter rỗng → "Không tìm thấy dữ liệu.") | Feedback QA/Reviewer |
| 2026-05-14 | v2.5 → v2.6 | §3.2 — Acceptance Criteria cập nhật | AC1 (Stat Banner), AC2 (Card fields cũ), AC3 (Download basic) | AC1 bổ sung count không đổi khi filter; AC2 cập nhật field mới theo thứ tự; AC3 bổ sung spinner+toast; AC4 mới: Empty State đúng ngữ cảnh | Feedback QA/Reviewer |
| 2026-05-14 | v2.6 → v2.7 | §2.1 — Khung Danh sách | Card List (5 trường) | Cập nhật theo UI mới: Đổi field 2 thành Mã báo cáo in đậm; Thêm field 4 "Tên báo cáo"; Đổi "Ngày tiếp nhận" thành "Ngày cập nhật" ở field Metadata. | Thiết kế Figma mới |
| 2026-05-14 | v2.6 → v2.7 | §2.1 — Modal Bộ lọc | Dropdown Trạng thái | Bổ sung thêm 2 filter: Loại báo cáo (lấy từ Master Data hệ thống) và Tỉnh/thành phố. | Thiết kế Figma mới |
| 2026-05-14 | v2.7 → v2.8 | §2.1 — Modal Bộ lọc | Hành động đóng Bottom Sheet | Bổ sung logic: Nhấn nút Back vật lý (Android) khi Bottom Sheet đang mở → Đóng Bottom Sheet (không thoát màn hình). | Feedback từ BA/QA |
| 2026-05-14 | v2.8 → v2.9 | Global | Text Empty State | Cập nhật đồng bộ text "Không tìm thấy kết quả" thành "Không tìm thấy dữ liệu". | Quyết định mới của Team |
| 2026-05-21 | v2.9 → v2.10 | Align CMR Mobile v6.0 | 1. Chuẩn hoá dropdown default 'Tất cả' |
| 2026-05-24 | v2.10 → v2.11 | Card List — Tên dự án: logic ẩn khi null | Không có quy tắc null | Nếu null → ẩn toàn bộ field (không hiển thị dòng này trên card) | Phương án B — không phải BC nào cũng có dự án |
| 2026-05-24 | v2.10 → v2.11 | Card List — Thêm field Cơ quan tiếp nhận | (Không có) | Thêm field #5: "Cơ quan tiếp nhận: " + Tên cơ quan. Tối đa 2 dòng, truncate. Nếu null → ẩn toàn bộ field | Theo design mới |
| 2026-05-24 | v2.10 → v2.11 | Card List — Metadata: logic ẩn linh hoạt | "Kỳ: [Giá trị] • Ngày cập nhật: [DD/MM/YYYY]" (luôn hiển thị) | Hiển thị linh hoạt: có cả 2 → full; chỉ có 1 → hiển thị phần có; cả 2 null → ẩn toàn bộ field | Theo design + logic ẩn khi null |
| 2026-05-24 | v2.10 → v2.11 | AC2 cập nhật | Thứ tự 6 field | Thứ tự 7 field + ghi chú logic ẩn khi null cho Tên dự án, Cơ quan tiếp nhận, Metadata | Đồng bộ Card List mới |
