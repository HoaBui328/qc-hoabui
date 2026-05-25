# CHỨC NĂNG CHUNG (COMMON FUNCTIONS - CF)

## Phân hệ Báo cáo | Hệ thống MBFS

> Tài liệu này định nghĩa các chức năng chung áp dụng xuyên suốt toàn bộ phân hệ Báo cáo.
> Mỗi CF là **Single Source of Truth** cho logic chức năng tương ứng.
> Các UC (Use Case) **phải tham chiếu CF** thay vì viết lại chi tiết chức năng chung.

---

## CF_01: Lập báo cáo (Create Report)

### Điều kiện hiển thị nút [Lập báo cáo]

- Kỳ hạn ở trạng thái **"Trong thời hạn"** → Hiển thị nút [Lập báo cáo] và [Nhập từ file]. Tham chiếu: CMR_04.
- Kỳ hạn ở trạng thái **"Chưa tới hạn"** → Ẩn nút. Không được phép tạo mới. Tham chiếu: CMR_04.
- Kỳ hạn ở trạng thái **"Qua kỳ báo cáo"** → Ẩn nút. Không được phép tạo mới. Tham chiếu: CMR_04.
- Với nhóm báo cáo ĐTNN/ĐTTN (1 dự án nhiều NĐT nhưng có tổ chức kinh tế phụ trách lập báo cáo): Chỉ TCKT (Tổ chức kinh tế) phụ trách mới thấy nút này. Các NĐT thành viên trong dự án → Ẩn nút. Tham chiếu: CMR_01.

### Luồng nghiệp vụ

- **Bước 1:** Người dùng nhấn nút [Lập báo cáo] tại màn hình Danh sách.
- **Bước 2:** Hệ thống mở form nhập liệu theo biểu mẫu tương ứng. Tất cả trường ở trạng thái trống. Các trường dữ liệu từ API giữ trạng thái Disabled cho đến khi chọn Phạm vi dữ liệu nguồn input. Tham chiếu: CMR_12.
- **Bước 3:** Người dùng nhập liệu. Có thể chọn Phạm vi dữ liệu nguồn input bất kỳ lúc nào.
- **Bước 4:** Hệ thống hiển thị các nút hành động: [Lưu nháp], [Xem trước], [Nộp báo cáo], [Hủy].

### Xử lý chọn Phạm vi dữ liệu nguồn input (Auto-fill API)

- Ngay khi chọn Phạm vi dữ liệu nguồn input từ Dropdown, hệ thống gọi API và tự động điền các trường dữ liệu liên quan.
- Trạng thái trường sau khi API phản hồi: Tham chiếu: CMR_12.
- Nếu người dùng chọn một Phạm vi dữ liệu nguồn input đã có bản ghi báo cáo được tạo bởi người dùng khác trong kỳ hiện tại → Hiển thị Toast lỗi — Tiêu đề: *"Báo cáo đã được lập"*, Nội dung: *"Báo cáo cho [Phạm vi dữ liệu nguồn input] đã chọn đã được lập bởi [Tên người lập]"*. Không cho phép tiếp tục tạo báo cáo cho Phạm vi này.
- Nếu gọi API thất bại: Hiển thị Toast lỗi — Tiêu đề: *"Lỗi hệ thống"*, Nội dung: *"Không thể kết nối đến hệ thống. Vui lòng thử lại sau."*. Các trường dữ liệu API giữ trạng thái trống và Disabled.

### Xử lý nút [Lưu nháp]

- Hệ thống auto-trim khoảng trắng các trường Text/Textarea.
- **Validate tối thiểu khi Lưu nháp** (không validate các trường bắt buộc khác — chỉ validate khi Nộp):
  - **Case 1 — Báo cáo CÓ Phạm vi dữ liệu nguồn input:** Bắt buộc phải chọn trường Phạm vi dữ liệu nguồn input trước khi lưu. Nếu chưa chọn → hiển thị lỗi inline màu đỏ bên dưới trường: *"Vui lòng chọn Phạm vi dữ liệu nguồn input"*. Dừng luồng, không lưu. Tham chiếu: CMR_07.
  - **Case 2 — Báo cáo KHÔNG CÓ Phạm vi dữ liệu nguồn input:** Bắt buộc ít nhất 1 trường thông tin phải có dữ liệu (bao gồm cả data auto-fill). Nếu tất cả các trường đều trống → hiển thị Toast lỗi — Tiêu đề: *"Lưu nháp không thành công"*, Nội dung: *"Bạn cần nhập dữ liệu cho trường thông tin trước khi lưu nháp"*. Dừng luồng, không lưu.
- Nếu thành công: Chuyển trạng thái thành "Lưu nháp". Hiển thị Toast thành công — Tiêu đề: *"Thành công"*, Nội dung: *"Đã lưu báo cáo thành công"*. Toast hiển thị góc trên bên phải, tự biến mất sau 3–5 giây. Giữ nguyên ở màn hình hiện tại.
- Nếu thất bại: Hiển thị Toast lỗi — Tiêu đề: *"Lỗi hệ thống"*, Nội dung: *"Không thể kết nối đến hệ thống. Vui lòng thử lại sau."*. Giữ nguyên màn hình, không mất dữ liệu đã nhập.

### Xử lý nút [Xem trước] (PDF Preview Popup)

- **Điều kiện hiển thị / trạng thái nút [Xem trước] tại màn hình Lập (CF_01):**
  - **Disabled (mờ, không thể nhấn):** Khi báo cáo **chưa được lưu nháp lần nào** — tức là bản ghi chưa tồn tại trong cơ sở dữ liệu. Hiển thị tooltip khi hover: *"Vui lòng Lưu nháp hoặc Nộp báo cáo trước khi xem preview."*
  - **Enabled (cho phép nhấn):** Sau khi báo cáo đã được **Lưu nháp** hoặc **Nộp** ít nhất 1 lần thành công — tức là bản ghi đã tồn tại trong cơ sở dữ liệu.
  - **Lưu ý:** Tại màn hình **Chỉnh sửa (CF_03)** và **Xem chi tiết (CF_07)**, nút [Xem trước] luôn **Enabled** vì bản ghi đã tồn tại trong hệ thống.
- Mở popup hiển thị dữ liệu đang nhập theo định dạng PDF (Read-only).
- Popup có icon Đóng (✕) ở góc trên bên phải thanh tiêu đề.
- Nội dung: Vùng xem preview biểu mẫu (có thanh cuộn).
- **Autofill thông tin Header/Footer của báo cáo:**
  - Địa điểm: theo thông tin địa chỉ của user đang đăng nhập.
  - Ngày tháng năm: ngày nộp báo cáo (ngày thực hiện thao tác).
  - Người làm báo cáo: Tên của user đang thực hiện.
  - ⚠️ **Lưu ý:** Tại thời điểm Preview, dữ liệu chưa được validate — các thông tin hiển thị có thể chưa chính xác hoặc chưa đầy đủ. Hệ thống vẫn hiển thị bình thường để người dùng xem trước.
- Khu vực footer: 1 nút hành động:
  - **[In]:** Mở Print Preview dạng PDF → mở hộp thoại in trình duyệt.
- **Phạm vi:** Popup PDF Preview chỉ khả dụng từ bên trong màn hình Tạo mới (CF_01), Chỉnh sửa (CF_03), và Xem (CF_07). Không trigger trực tiếp từ cột Hành động trên Danh sách. Tham chiếu: CF_07.1.

### Xử lý nút [Nộp báo cáo]

- **Bước 1 — Validate:** Hệ thống auto-trim và validate tất cả trường bắt buộc. Nếu thiếu: hiển thị lỗi inline màu đỏ *"Vui lòng nhập/chọn [tên trường]"* tại từng trường lỗi. Tham chiếu: CMR_05, CMR_06, CMR_07. Dừng luồng, không mở popup.
- **Bước 2 — Popup xác nhận:** Nếu tất cả validate hợp lệ, hiển thị popup xác nhận:
  - Tiêu đề: *"Bạn có chắc muốn nộp?"*
  - Nội dung: Checkbox bắt buộc tích trước khi nhấn [Xác nhận]: *"Tôi đã kiểm tra toàn bộ thông tin đã nhập và xác nhận rằng các thông tin đó là chính xác."*
  - Nút [Xác nhận] — Chỉ active khi checkbox đã được tích. Nhấn → thực hiện nộp.
  - Nút [Hủy] — Đóng popup, quay lại form (không mất dữ liệu).
  - Icon Đóng (✕) góc trên bên phải → tương đương nhấn [Hủy].
- **Bước 3 — Nộp thành công:** Chuyển trạng thái thành "Đã tiếp nhận" hoặc "Chờ duyệt" (theo CMR_03). Hiển thị Toast thành công — Tiêu đề: *"Thành công"*, Nội dung: *"Đã nộp báo cáo thành công"*. Quay lại màn hình Danh sách.
- **Nộp thất bại:** Hiển thị Toast lỗi — Tiêu đề: *"Lỗi hệ thống"*, Nội dung: *"Không thể kết nối đến hệ thống. Vui lòng thử lại sau."*. Giữ nguyên màn hình.

### Xử lý nút [Hủy]

- Hệ thống kiểm tra trạng thái form (dirty check). Nếu form không dirty (người dùng chưa thay đổi bất kỳ field nào), hệ thống quay lại Danh sách ngay lập tức mà không hiển thị popup.
- Nếu form đang dirty (có dữ liệu chưa lưu), hệ thống hiển thị popup cảnh báo:
  - Tiêu đề: *"Dữ liệu chưa được lưu"*
  - Nội dung: *"Bạn có chắc chắn muốn rời khỏi trang này không?"*
  - Nút **[Đồng ý]** → Đóng form, quay lại màn hình Danh sách. Dữ liệu chưa lưu bị hủy bỏ.
  - Nút **[Hủy]** → Đóng popup, ở lại form. Dữ liệu trên form được giữ nguyên.
- Tham chiếu: CMR_14.

---

<mark>

## CF_01.1: Áp dụng cho Báo cáo gộp — Lập báo cáo (CF_01)

> **Bổ sung mới — 2026-04-21 | UC011-034**
> Các hành vi sau đây khác biệt so với báo cáo đơn lẻ khi áp dụng CF_01 cho Báo cáo gộp.

### [Lưu nháp]

- Lưu nháp lưu dữ liệu của **toàn bộ N biểu (tabs)** trong Bộ hồ sơ cùng lúc — không chỉ tab đang mở.
- **Validate tối thiểu khi Lưu nháp** — validate **từng tab độc lập** (không validate cross-tab, không validate các trường bắt buộc khác — chỉ validate khi Nộp):
  - **Case 1 — Biểu CÓ Phạm vi dữ liệu nguồn input:** Bắt buộc phải chọn trường Phạm vi dữ liệu nguồn input của biểu đó trước khi lưu. Nếu chưa chọn → lỗi inline *”Trường bắt buộc”* + badge đỏ trên tab header của biểu lỗi. Dừng luồng, không lưu bất kỳ tab nào.
  - **Case 2 — Biểu KHÔNG CÓ Phạm vi dữ liệu nguồn input:** Bắt buộc ít nhất 1 trường thông tin phải có dữ liệu (bao gồm cả data auto-fill). Nếu tất cả trống → lỗi inline + badge đỏ trên tab header của biểu lỗi. Dừng luồng, không lưu bất kỳ tab nào.
  - **Hiển thị lỗi cross-tab:** Nếu nhiều tab lỗi đồng thời, badge đỏ hiển thị trên tất cả tab header có lỗi. Người dùng tự chuyển tab để xem và sửa.
- **Counter “Số báo cáo đang xử lý”:** Biểu chỉ được tính vào counter trên màn hình Danh sách khi đã Lưu nháp thành công ít nhất 1 lần (có data).
- Nếu Bộ hồ sơ đang ở trạng thái “Yêu cầu chỉnh sửa” → sau khi Lưu nháp thành công, trạng thái **giữ nguyên** “Yêu cầu chỉnh sửa” (không về “Lưu nháp”). Tham chiếu: CF_03.1.
- Toast thành công — Tiêu đề: *”Thành công”*, Nội dung: *”Đã lưu Bộ hồ sơ thành công”*. Giữ nguyên ở màn hình hiện tại (không quay lại Danh sách — khác với báo cáo đơn lẻ CF_01).
- Lưu thất bại (lỗi server): Toast lỗi — Tiêu đề: *”Lỗi hệ thống”*, Nội dung: *”Không thể kết nối đến hệ thống. Vui lòng thử lại sau.”*. Giữ nguyên màn hình, không mất dữ liệu đã nhập trên tất cả tabs.

### Chuyển tab biểu mẫu nội bộ

- Dữ liệu nhập liệu được giữ **in-memory** khi chuyển giữa các tab trong cùng Bộ hồ sơ. Người dùng chuyển tab tự do mà không mất dữ liệu chưa lưu.
- **Không hiển thị popup cảnh báo** khi chuyển tab nội bộ (khác với phiên bản trước).
- Dữ liệu in-memory chỉ bị mất khi: (1) người dùng rời khỏi màn hình báo cáo (nhấn [Hủy]), (2) đóng trình duyệt, hoặc (3) mất kết nối.

### Nút [Hủy] — Rời khỏi màn hình Báo cáo gộp

- Hệ thống kiểm tra dirty check trên **toàn bộ N tabs** (không chỉ tab đang mở). Nếu BẤT KỲ tab nào có thay đổi chưa lưu so với lần load/lưu gần nhất → form được coi là dirty.
- Nếu form dirty: Hiển thị popup cảnh báo:
  - Tiêu đề: *”Dữ liệu chưa được lưu”*
  - Nội dung: *”Bạn có chắc chắn muốn rời khỏi trang này không?”*
  - Nút **[Đồng ý]** → Đóng form, quay lại màn hình Danh sách. Dữ liệu chưa lưu trên **tất cả tabs** bị hủy bỏ.
  - Nút **[Hủy]** → Đóng popup, ở lại form. Dữ liệu trên tất cả tabs được giữ nguyên.
- Nếu form không dirty (tất cả tabs đều chưa thay đổi hoặc đã lưu): Quay lại Danh sách ngay lập tức, không hiển thị popup.
- Tham chiếu: CMR_14.

### [Nộp báo cáo] — Toàn Bộ hồ sơ

- Nút [Nộp báo cáo] chỉ xuất hiện ở biểu cuối cùng trong Bộ hồ sơ (không phải từng biểu).
- Khi nhấn [Nộp báo cáo]: Hệ thống auto-trim và validate tất cả N Tab đồng thời (cross-tab validation).
- Nếu có lỗi: Hiển thị **badge/indicator đỏ trên tab header** của tab có lỗi. Người dùng tự chuyển tab để xem và sửa. Lỗi inline màu đỏ hiển thị ngay dưới từng trường vi phạm.
- Nếu tất cả hợp lệ: Hiển thị Popup xác nhận Nộp (theo mục "Xử lý nút [Nộp báo cáo]" trong CF_01).
- Nộp thành công: Toàn bộ Bộ hồ sơ (N biểu) chuyển trạng thái sang "Chờ duyệt" hoặc "Đã tiếp nhận" (theo CMR_03). Toast thành công — Tiêu đề: *"Thành công"*, Nội dung: *"Đã nộp báo cáo thành công"*. Quay lại màn hình Danh sách.

---

## CF_02: Nhập báo cáo từ file (Nhập từ file Report)

Nhập từ file hiển thị dưới dạng Popup với icon Đóng [✕] và nút [Hủy].

### Điều kiện hiển thị nút [Nhập từ file]

- Kỳ hạn **"Trong thời hạn"** → Hiển thị. **"Chưa tới hạn"** hoặc **"Qua kỳ báo cáo"** → Ẩn. Không được phép nhập từ file. Tham chiếu: CMR_04.
- Case A (ĐTNN/ĐTTN): Chỉ TCKT phụ trách mới thấy nút này. Các NĐT thành viên → Ẩn nút. Tham chiếu: CMR_01.

### Case 1: Báo cáo có Phạm vi dữ liệu nguồn input bắt buộc

**Bao gồm:**

\-      Báo cáo có phạm vi đơn (Single-scope): 1 báo cáo - 1 phạm vi

\-      Báo cáo có phạm vi đa dòng (Multi-scope): 1 báo cáo - N phạm vi (mỗi dòng trong bảng)

**Bước 1 — Chọn Phạm vi dữ liệu nguồn input:**

*   Người dùng chọn Phạm vi dữ liệu nguồn input từ Dropdown.

    *   Với Báo cáo có phạm vi đơn: dropdown dạng single choice
    *   Với báo cáo có phạm vi đa dòng: dropdown dạng multiple choice, các giá trị dạng liệt kê dạng flat

*   Nếu người dùng chọn một Phạm vi dữ liệu nguồn input đã có bản ghi báo cáo được tạo bởi người dùng khác trong kỳ hiện tại → Hiển thị Toast lỗi. Không cho phép tiếp tục.

**Bước 2 — Tải Template:**

*   Khi chưa chọn Phạm vi: Các chức năng Tải/Upload bị Disabled.
*   Sau khi chọn Phạm vi: Hệ thống tạo template điền sẵn Master Data. Với báo cáo có phạm vi đa dòng thì các phạm được chọn sẽ được hệ thống tự động phân loại theo section nếu được định nghĩa trong tài liệu báo cáo (Ví dụ Biểu mẫu 2112, Tên khu sẽ được phân theo các section là Đang vận hành và Đang xây dung cơ bản)
*   Người dùng tải về. Tên file được đặt theo quy tắc: Mau\_\[Mã-báo-cáo\]\_\[YYYYMMDD\]\_\[HHMM\]. (Ví dụ: Mau\_A-IV-4\_20260425\_2004).
*   Người dùng tiến hành nhập liệu trên file, lưu ý: các trường đã được hệ thống điền sẵn từ Master data sẽ bị khóa (không được sửa). Với báo cáo có phạm vi đa dòng, nếu user muốn thêm/ bớt phạm vi áp dụng thì cần phải quay lại Bước 1 để thêm/ bớt phạm vi và tải lại file

**Bước 3 — Upload File:**

- Validate dữ liệu: Nếu dữ liệu trong file không khớp với Phạm vi dữ liệu nguồn input đã chọn → Giữ nguyên popup, hiển thị Alert: *"Dữ liệu không khớp với [Phạm vi dữ liệu nguồn input] đã chọn. Vui lòng kiểm tra lại."*
- Validate cấu trúc template: Nếu file đúng định dạng nhưng cấu trúc không khớp → Giữ nguyên popup, hiển thị Alert: *"Cấu trúc file không đúng định dạng template. Vui lòng sử dụng file template đã tải."*
- File sai định dạng → Giữ nguyên popup, hiển thị Alert: *"Định dạng file không được hỗ trợ. Vui lòng sử dụng file template đã tải."*
- File rỗng / không đọc được → Giữ nguyên popup, hiển thị Alert: *"Không thể đọc file. Vui lòng kiểm tra lại file và thử lại."*
- Lỗi server khi upload → Toast lỗi — Tiêu đề: *"Lỗi hệ thống"*, Nội dung: *"Không thể kết nối đến hệ thống. Vui lòng thử lại sau."*
- UI file đã upload: Component file đã upload phải có icon "Xóa/Đóng" để cho phép loại bỏ file và chọn lại.
- **Validate nội dung autofill:** Hệ thống đối chiếu nội dung các field được autofill trong file với dữ liệu hiện tại trên hệ thống.
  - Nếu không khớp: Giữ nguyên popup, hiển thị Alert: *"Dữ liệu đã được cập nhật. Vui lòng tải lại file mẫu mới."* Đồng thời hệ thống tự động cập nhật dữ liệu mới nhất vào file mẫu để người dùng tải lại.
  - Nếu khớp: Upload thành công — Đóng popup Nhập từ file, chuyển đến màn hình Tạo mới báo cáo. Dữ liệu từ file được map vào các trường tương ứng trên form.
- **Cách upload:** Click vào khu vực upload để mở File Explorer, hoặc kéo thả file trực tiếp vào khu vực đó. Hệ thống tự động lọc file không đúng định dạng.
- Trạng thái trường sau upload: Các trường Master Data (nguồn từ API) → Disabled. Tất cả trường nhập liệu khác → Enabled cho phép chỉnh sửa.
- Các nút hành động: Chuyển về chế độ Tạo mới tiêu chuẩn: [Xem chi tiết], [Lưu nháp], [Nộp báo cáo], [Hủy].
### Case 2: Báo cáo không có Phạm vi dữ liệu nguồn input

**Mô tả màn hình:**

| Loại báo cáo | Giao diện popup |
| :--- | :--- |
| **Báo cáo lẻ** | 1 vùng upload duy nhất. Người dùng tải file mẫu về, điền thông tin, rồi click hoặc kéo thả file vào vùng upload. Hệ thống tự động lọc file sai định dạng. |
| **Báo cáo theo bộ** | Vùng upload riêng cho **từng biểu mẫu**. Người dùng tải file mẫu của từng biểu về và upload vào slot tương ứng. Hệ thống tự lọc file sai định dạng. Nút [Tiếp tục] mặc định Disabled — chỉ Enable khi người dùng upload đủ số file hợp lệ cho tất cả các biểu. |

**Bước 1 — Tải Template:**

- Hệ thống cung cấp template chuẩn (không điền sẵn Master Data). Người dùng tải file template về máy. Tên file được đặt theo quy tắc: `Mau_[Mã-báo-cáo]_[YYYYMMDD]_[HHMM]`. (Ví dụ: `Mau_A-IV-4_20260425_2004`).

**Bước 2 — Upload File:**

Với từng file upload lên, hệ thống sẽ thực hiện validate như sau:

- Validate cấu trúc template: Nếu file đúng định dạng (`.docx` / `.xlsx`) nhưng cấu trúc không khớp với template quy định → Giữ nguyên popup, hiển thị Alert: *"Cấu trúc file không đúng định dạng template. Vui lòng sử dụng file template đã tải."*
- File sai định dạng → Giữ nguyên popup, hiển thị Alert: *"Định dạng file không được hỗ trợ. Vui lòng sử dụng file template đã tải."*
- File rỗng / không đọc được → Giữ nguyên popup, hiển thị Alert: *"Không thể đọc file. Vui lòng kiểm tra lại file và thử lại."*
- Lỗi server khi upload → Toast lỗi — Tiêu đề: *"Lỗi hệ thống"*, Nội dung: *"Không thể kết nối đến hệ thống. Vui lòng thử lại sau."*
- UI file đã upload: Component file đã upload phải có icon "Xóa/Đóng" để cho phép loại bỏ file và chọn lại.

**Upload thành công — xử lý theo loại báo cáo:**

- **Báo cáo lẻ:** Hệ thống tự động đóng popup Nhập từ file, chuyển đến màn hình Tạo mới báo cáo. Dữ liệu từ file được map vào các trường tương ứng trên form màn Lập báo cáo. Tất cả trường nhập liệu → Enabled cho phép chỉnh sửa.
- **Báo cáo theo bộ (Báo cáo gộp):** Khi người dùng upload đủ số file hợp lệ → hệ thống Enable nút [Tiếp tục] → Người dùng nhấn [Tiếp tục] → Hệ thống đóng popup Nhập từ file, chuyển đến màn hình Tạo mới báo cáo (focus vào tab báo cáo đầu tiên). Dữ liệu từ file được map vào các trường tương ứng trên form màn Lập báo cáo và tương ứng với các tab của báo cáo. Tất cả trường nhập liệu → Enabled cho phép chỉnh sửa.
- Các nút hành động sau nhập từ file: [Xem chi tiết], [Lưu nháp], [Nộp báo cáo], [Hủy].

### Edge cases (cả 2 cases)

- Người dùng nhấn [Hủy] hoặc icon [✕] bất kỳ lúc nào trên popup → Đóng popup, quay lại Danh sách, không thực hiện nhập từ file.
- Nếu người dùng upload file thành công rồi nhấn [Hủy] trên màn hình Tạo mới → Dữ liệu nhập từ file bị hủy, không lưu bản ghi. Quay lại Danh sách.

---

## CF_03: Chỉnh sửa báo cáo (Edit Report)

### Điều kiện hiển thị nút [Chỉnh sửa]

- Bản ghi ở trạng thái "Lưu nháp" hoặc "Yêu cầu chỉnh sửa" → Hiển thị nút. Tham chiếu: CMR_03.
- Bản ghi ở trạng thái "Chờ duyệt" hoặc "Đã tiếp nhận" → Ẩn nút. Tham chiếu: CMR_03.
- Case A (ĐTNN/ĐTTN): Chỉ TCKT phụ trách mới có quyền [Chỉnh sửa]. Các NĐT thành viên → Ẩn nút, chỉ có quyền Xem. Tham chiếu: CMR_01.
- Case B (ĐTRNN): Tất cả NĐT trong dự án (kể cả NĐT không phải người khởi tạo) đều có quyền [Chỉnh sửa] khi bản ghi ở trạng thái cho phép (Lưu nháp / Yêu cầu chỉnh sửa). Thao tác ghi vào Lifecycle Log. Tham chiếu: CMR_02.

### Luồng nghiệp vụ

- **Bước 1:** Người dùng nhấn [Chỉnh sửa] tại cột Hành động trên Danh sách.
- **Bước 2:** Hệ thống mở lại form nhập liệu, điền sẵn dữ liệu hiện tại của bản ghi.
- **Bước 3:** Hệ thống hiển thị các nút hành động: [Lưu nháp], [Nộp báo cáo], [Xem trước], [Hủy].
- Trạng thái trường: Các trường Master Data / dữ liệu từ API → theo CMR_12. Các trường nhập liệu khác → Enabled.

### Trạng thái nút [Lưu nháp] và [Nộp báo cáo] theo trạng thái bản ghi

- **Bản ghi ở trạng thái "Lưu nháp":** Nút [Lưu nháp] và [Nộp báo cáo] luôn **Enabled**.
- **Bản ghi ở trạng thái "Yêu cầu chỉnh sửa":** Nút [Lưu nháp] và [Nộp báo cáo] mặc định **Disabled** khi form chưa dirty. Tooltip khi hover:
  - [Nộp báo cáo]: *"Vui lòng chỉnh sửa ít nhất một trường thông tin trước khi nộp."*
  - [Lưu nháp]: *"Vui lòng chỉnh sửa ít nhất một trường thông tin trước khi lưu nháp."*
  - Cả hai nút chuyển sang **Enabled** ngay khi người dùng thay đổi bất kỳ field nào (form dirty). Tham chiếu: CMR_14.

### Xử lý nút [Lưu nháp] — Quy tắc bảo toàn trạng thái

- Hệ thống auto-trim khoảng trắng các trường Text/Textarea.
- **Validate tối thiểu khi Lưu nháp** (không validate các trường bắt buộc khác — chỉ validate khi Nộp):
  - **Case 1 — Báo cáo CÓ Phạm vi dữ liệu nguồn input:** Bắt buộc phải chọn trường Phạm vi dữ liệu nguồn input trước khi lưu. Nếu chưa chọn → hiển thị lỗi inline màu đỏ bên dưới trường: *"Vui lòng chọn Phạm vi dữ liệu nguồn input"*. Dừng luồng, không lưu. Tham chiếu: CMR_07.
  - **Case 2 — Báo cáo KHÔNG CÓ Phạm vi dữ liệu nguồn input:** Bắt buộc ít nhất 1 trường thông tin phải có dữ liệu (bao gồm cả data auto-fill). Nếu tất cả các trường đều trống → hiển thị Toast lỗi — Tiêu đề: *"Lưu nháp không thành công"*, Nội dung: *"Bạn cần nhập dữ liệu cho trường thông tin trước khi lưu nháp"*. Dừng luồng, không lưu.
- Nếu bản ghi đang ở trạng thái "Lưu nháp": Lưu thành công → trạng thái vẫn là "Lưu nháp". Hiển thị Toast thành công — Tiêu đề: *"Thành công"*, Nội dung: *"Đã chỉnh sửa báo cáo thành công"*. Giữ nguyên ở màn hình hiện tại.
- Nếu bản ghi đang ở trạng thái "Yêu cầu chỉnh sửa": Lưu thành công → trạng thái giữ nguyên là "Yêu cầu chỉnh sửa", không chuyển sang "Lưu nháp". Hiển thị Toast thành công — Tiêu đề: *"Thành công"*, Nội dung: *"Đã chỉnh sửa báo cáo thành công"*. Giữ nguyên ở màn hình hiện tại.
- Lưu thất bại: Hiển thị Toast lỗi — Tiêu đề: *"Lỗi hệ thống"*, Nội dung: *"Không thể kết nối đến hệ thống. Vui lòng thử lại sau."*. Giữ nguyên màn hình, không mất dữ liệu.

### Xử lý nút [Nộp báo cáo]

- **Bước 1 — Validate:** Hệ thống auto-trim và validate tất cả trường bắt buộc. Nếu thiếu: hiển thị lỗi inline màu đỏ *"Vui lòng nhập/chọn [tên trường]"* tại từng trường lỗi. Tham chiếu: CMR_05, CMR_06, CMR_07. Dừng luồng, không mở popup.
- **Bước 2 — Popup xác nhận:** Nếu tất cả validate hợp lệ, hiển thị popup xác nhận:
  - Tiêu đề: *"Bạn có chắc muốn nộp?"*
  - Nội dung: Checkbox bắt buộc tích trước khi nhấn [Xác nhận]: *"Tôi đã kiểm tra toàn bộ thông tin đã nhập và xác nhận rằng các thông tin đó là chính xác."*
  - Nút [Xác nhận] — Chỉ active khi checkbox đã được tích. Nhấn → thực hiện nộp.
  - Nút [Hủy] — Đóng popup, quay lại form (không mất dữ liệu).
  - Icon Đóng (✕) góc trên bên phải → tương đương nhấn [Hủy].
- **Bước 3 — Nộp thành công:** Chuyển trạng thái thành "Đã tiếp nhận" hoặc "Chờ duyệt" (theo CMR_03) (bất kể trạng thái trước đó là "Lưu nháp" hay "Yêu cầu chỉnh sửa"). Hiển thị Toast thành công — Tiêu đề: *"Thành công"*, Nội dung: *"Đã nộp báo cáo thành công"*. Quay lại màn hình Danh sách.
- **Nộp thất bại:** Hiển thị Toast lỗi — Tiêu đề: *"Lỗi hệ thống"*, Nội dung: *"Không thể kết nối đến hệ thống. Vui lòng thử lại sau."*. Giữ nguyên màn hình.

### Xử lý nút [Xem trước] (PDF Preview Popup)

- **Điều kiện trạng thái nút [Xem trước] tại màn hình Chỉnh sửa (CF_03):** Luôn **Enabled** — bản ghi đã tồn tại trong cơ sở dữ liệu (đã lưu nháp hoặc đã nộp ít nhất 1 lần). Tham chiếu: CF_01 — điều kiện enable nút.
- Mở popup hiển thị dữ liệu đang nhập theo định dạng PDF (Read-only).
- Popup có icon Đóng (✕) ở góc trên bên phải thanh tiêu đề.
- Nội dung: Vùng xem preview biểu mẫu (có thanh cuộn).
- Khu vực footer: 1 nút hành động:
  - **[In]:** Mở Print Preview dạng PDF → mở hộp thoại in trình duyệt.
- **Phạm vi:** Popup PDF Preview chỉ khả dụng từ bên trong màn hình Tạo mới (CF_01), Chỉnh sửa (CF_03), và Xem chi tiết (CF_07). Không trigger trực tiếp từ cột Hành động trên Danh sách.

### Xử lý nút [Hủy]

- Hệ thống kiểm tra trạng thái form (dirty check). Nếu form không dirty (người dùng chưa thay đổi bất kỳ field nào kể từ lần load/lưu gần nhất), hệ thống quay lại Danh sách ngay lập tức mà không hiển thị popup.
- Nếu form đang dirty (có thay đổi chưa lưu), hệ thống hiển thị popup cảnh báo:
  - Tiêu đề: *"Dữ liệu chưa được lưu"*
  - Nội dung: *"Bạn có chắc chắn muốn rời khỏi trang này không?"*
  - Nút **[Đồng ý]** → Đóng form, quay lại màn hình Danh sách. Dữ liệu chưa lưu bị hủy bỏ, bản ghi quay về trạng thái và dữ liệu lần lưu gần nhất.
  - Nút **[Hủy]** → Đóng popup, ở lại form. Dữ liệu trên form được giữ nguyên.
- Tham chiếu: CMR_14.

### Edge cases

- Người dùng mở chỉnh sửa nhưng không thay đổi gì → nhấn [Lưu nháp] → Hệ thống vẫn thực hiện lưu (có thể cập nhật thời gian sửa đổi), trạng thái bảo toàn.
- Người dùng mở chỉnh sửa, thay đổi dữ liệu, nhưng đóng trình duyệt / mất kết nối → Dữ liệu chưa lưu bị mất.

---

<mark>

## CF_03.1: Áp dụng cho Báo cáo gộp — Chỉnh sửa báo cáo (CF_03)

> **Bổ sung mới — 2026-04-21 | UC011-034**

- **Yêu cầu chỉnh sửa áp dụng toàn Bộ hồ sơ:** Khi Bộ hồ sơ nhận "Yêu cầu chỉnh sửa", yêu cầu áp dụng cho toàn package — người dùng có thể chỉnh sửa bất kỳ biểu nào trong Bộ hồ sơ.
- **Bảo toàn trạng thái khi Lưu nháp từng biểu:** Khi người dùng Lưu nháp một biểu đơn lẻ trong trạng thái "Yêu cầu chỉnh sửa", trạng thái Bộ hồ sơ **giữ nguyên** "Yêu cầu chỉnh sửa" — không chuyển về "Lưu nháp".
- Trạng thái Bộ hồ sơ chỉ được cập nhật khi người dùng nhấn [Nộp] thành công (từ biểu cuối hoặc từ Màn hình danh sách). Tham chiếu: CF_01.1.

</mark>

---

## CF_04: Kết xuất file (Xuất báo cáo)

### Điều kiện hiển thị

Nút [Xuất báo cáo] hiển thị ở tất cả trạng thái bản ghi, cho tất cả người dùng có quyền xem. Tham chiếu: CMR_03.

### Luồng nghiệp vụ

- **Bước 1:** Người dùng nhấn [Xuất báo cáo] tại cột Hành động trên Danh sách, hoặc nhấn [Xuất báo cáo] trong footer popup Xem chi tiết.
- **Bước 2:** Hệ thống tạo file .docx hoặc .xlsx (tùy theo biểu mẫu quy định) theo đúng biểu mẫu.
- **Bước 3:** File được tải xuống tự động vào thư mục Downloads mặc định của trình duyệt. Tên file kết xuất được đặt theo quy tắc:
  - **Với báo cáo NĐT tư nộp:** `[Mã-Báo-Cáo]_[Kỳ-Báo-Cáo]_[Mã-dự-án]` (Ví dụ: `ODI-I15-1_ky-1-2026_DA-XYZ`).
  - **Với báo cáo cơ quan ban ngành nộp:** `[Mã-Báo-Cáo]_[Kỳ-Báo-Cáo]_[Mã-cơ-quan-nộp]` (Ví dụ: `ODI-I15-1_ky-1-2026_BQLKCN`).

### Kết quả

- Kết xuất thành công: Hiển thị Toast thành công — Tiêu đề: *"Thành công"*, Nội dung: *"Đã xuất báo cáo thành công"*. Toast hiển thị góc trên bên phải, tự biến mất sau 3–5 giây.
- Kết xuất thất bại: Hiển thị Toast lỗi — Tiêu đề: *"Lỗi hệ thống"*, Nội dung: *"Không thể kết nối đến hệ thống. Vui lòng thử lại sau."*

### Edge cases

- Trình duyệt chặn download → Phụ thuộc vào thiết lập trình duyệt, hệ thống không kiểm soát.

---

<mark>

## CF_04.1: Áp dụng cho Báo cáo gộp — Kết xuất file (CF_04)

> **Bổ sung mới — 2026-04-21 | UC011-034**
> Xuất báo cáo Báo cáo gộp có 2 scope khác nhau tùy vào nơi trigger:

| Trigger từ                                              | Scope Xuất báo cáo                                       | Số file                                    |
| :------------------------------------------------------- | :------------------------------------------------- | :------------------------------------------ |
| Cột Hành động — màn hình Danh sách               | Xuất**toàn bộ N biểu** trong Bộ hồ sơ | N file .docx riêng lẻ (mỗi biểu 1 file) |
| Nút [Xuất báo cáo] trong Popup Preview (nút [Xem trước] từng Tab) | Xuất**chỉ biểu đang xem**                | 1 file .docx                                |

- Biểu chưa có dữ liệu (chưa Lưu nháp) → **vẫn được xuất** dưới dạng file trắng (blank template).
- Toast khi Xuất báo cáo tách rời N file từ Màn hình danh sách — Tiêu đề: *"Thành công"*, Nội dung: *"Đã xuất báo cáo [N] báo cáo thành công"*.

</mark>

---

## CF_05: In báo cáo (Print)

### Điều kiện hiển thị

Nút [In] hiển thị ở tất cả trạng thái bản ghi, cho tất cả người dùng có quyền xem. Tham chiếu: CMR_03.

### Luồng nghiệp vụ

- **Bước 1:** Người dùng nhấn [In] tại cột Hành động trên Danh sách, hoặc nhấn [In] trong footer popup Xem chi tiết.
- **Bước 2:** Hệ thống mở Print Preview ở định dạng PDF.
- **Bước 3:** Hệ thống mở hộp thoại in của trình duyệt (browser print dialog).

### Edge cases

- Người dùng đóng hộp thoại in mà không in → Không có hậu quả, quay lại màn hình trước đó.

---

<mark>

## CF_05.1: Áp dụng cho Báo cáo gộp — In báo cáo (CF_05)

> **Bổ sung mới — 2026-04-21 | UC011-034**
> In Báo cáo gộp có 2 scope khác nhau tùy vào nơi trigger:

| Trigger từ                                          | Scope In                                        | Kết quả  |
| :--------------------------------------------------- | :---------------------------------------------- | :--------- |
| Cột Hành động — màn hình Danh sách           | In**toàn bộ N biểu** trong Bộ hồ sơ | N file PDF |
| Nút [In] trong Popup Preview (nút [Xem trước] từng Tab) | In**chỉ biểu đang xem**                | 1 file PDF |

</mark>

---

## CF_06: Xem vòng đời (Audit Trail)

### Điều kiện hiển thị

Nút [Xem vòng đời] hiển thị ở tất cả trạng thái bản ghi, cho tất cả người dùng có quyền xem. Tham chiếu: CMR_03.

### Luồng nghiệp vụ

- **Bước 1:** Người dùng nhấn [Xem vòng đời] tại cột Hành động trên Danh sách.
- **Bước 2:** Hệ thống mở popup hiển thị Timeline lịch sử thao tác (bao gồm tất cả các lịch sử mà người dùng thực hiện, bao gồm: các hành động làm thay đổi trạng thái của báo cáo/ không thay đổi trạng thái của báo cáo (không tính đến các action ngoài quy trình nộp báo cáo như: xem, preview, in, xuất..)), sắp xếp theo thời gian giảm dần (mới nhất ở trên, cũ nhất ở dưới).

### Cấu trúc popup

- Icon Đóng (✕): Góc trên bên phải thanh tiêu đề. Nhấn → Đóng popup.
- Nội dung Timeline — Các thành phần của 1 log:

| STT | Thành phần | Mô tả | Ghi chú |
|-----|-----------|-------|---------|
| 1 | Thời gian | DD/MM/YYYY HH:MM | Luôn có ở mọi log |
| 2 | Trạng thái | Là trạng thái mới nhất của báo cáo | Luôn có ở mọi log |
| 3 | Người thực hiện | <Họ và tên người thực hiện thao tác> - Role | Luôn có ở mọi log |
| 4 | Hành động | Tùy thuộc vào từng case sẽ có format khác nhau (xem Bảng Chú thích bên dưới) | Luôn có ở mọi log |
| 5 | Lý do | Lý do người dùng nhập khi từ chối báo cáo | Chỉ có khi người dùng thực hiện từ chối báo cáo |
| 6 | Ảnh data snapshot | Định dạng ảnh, bao gồm ảnh chụp màn hình trước và sau khi người dùng thao tác làm data thay đổi | Chỉ có với các trường hợp 8-11 trong Bảng Giải thích các trạng thái, với mục 6 này sẽ update khi dev input tính khả thi |

- Chú thích format hành động:

| STT | Trạng thái đầu | Trạng thái sau | Format hành động |
|-----|----------------|----------------|-----------------|
| 1 | Lưu nháp | Chờ duyệt | Nộp báo cáo cho <role tiếp nhận báo cáo - cơ quan tiếp nhận báo cáo theo quy trình> |
| 2 | Lưu nháp | Đã tiếp nhận | Nộp báo cáo cho <role tiếp nhận báo cáo - cơ quan tiếp nhận báo cáo theo quy trình> |
| 3 | Lưu nháp | Lưu nháp | Chỉnh sửa báo cáo và lưu nháp |
| 4 | Chờ duyệt | Đã tiếp nhận | Phê duyệt và nộp báo cáo cho <role tiếp nhận báo cáo - cơ quan tiếp nhận báo cáo theo quy trình> |
| 5 | Chờ duyệt | Yêu cầu chỉnh sửa | Từ chối báo cáo |
| 6 | Chờ duyệt | Chờ duyệt | Phê duyệt và nộp báo cáo đến <role tiếp nhận báo cáo - cơ quan tiếp nhận báo cáo theo quy trình> |
| 7 | Đã tiếp nhận | Yêu cầu chỉnh sửa | Từ chối báo cáo |
| 8 | Đã tiếp nhận | Đã tiếp nhận | Chỉnh sửa báo cáo |
| 9 | Yêu cầu chỉnh sửa | Chờ duyệt | Thực hiện chỉnh sửa và nộp lại cho <role tiếp nhận báo cáo - cơ quan tiếp nhận báo cáo theo quy trình> |
| 10 | Yêu cầu chỉnh sửa | Đã tiếp nhận | Thực hiện chỉnh sửa và nộp lại <role tiếp nhận báo cáo - cơ quan tiếp nhận báo cáo theo quy trình> |
| 11 | Yêu cầu chỉnh sửa | Yêu cầu chỉnh sửa | Thực hiện chỉnh sửa và lưu nháp |
| 12 | (Không có) | Lưu nháp | Tạo mới báo cáo và lưu nháp |

- Hiển thị: dạng lazy load
- Màn hình tham chiếu: https://www.figma.com/design/cklcaM2w5S8To691104P3j/C%E1%BB%95ng-%C4%91%E1%BA%A7u-t%C6%B0-QG---B%C3%A1o-c%C3%A1o?node-id=8211-1000&t=qpm0MOdtCsoqAgcQ-4

### Giải thích các trạng thái

Bảng giải thích sự thay đổi của các trạng thái báo cáo:

| STT | Trạng thái đầu | Trạng thái sau | Hành động user | Hệ thống lưu log |
|-----|----------------|----------------|----------------|-------------------|
| 1 | Lưu nháp | Chờ duyệt | Khi user ấn Nộp báo cáo (với trường hợp quy trình có > 2 bước) | **Thời gian:** 10/03/2026 15:30 / **Trạng thái:** Chờ duyệt / **Người thực hiện:** <Nguyễn Văn A> - Nhà đầu tư / **Action:** Nộp báo cáo cho Cán bộ chuyên môn khu |
| 2 | Lưu nháp | Đã tiếp nhận | Khi user ấn Nộp báo cáo (với trường hợp quy trình có 2 bước) | **Thời gian:** 10/03/2026 15:30 / **Trạng thái:** Đã tiếp nhận / **Người thực hiện:** Nguyễn Văn A - Nhà đầu tư / **Action:** Nộp báo cáo cho Cục đầu tư Nước Ngoài |
| 3 | Lưu nháp | Lưu nháp | User chỉnh sửa báo cáo lưu nháp và lưu nháp tiếp | **Thời gian:** 10/03/2026 15:30 / **Trạng thái:** Lưu nháp / **Người thực hiện:** Nguyễn Văn A - Nhà đầu tư / **Action:** Chỉnh sửa báo cáo và lưu nháp |
| 4 | Chờ duyệt | Đã tiếp nhận | Khi cơ quan trung gian ấn phê duyệt đẩy báo cáo lên cơ quan cuối cùng nhận báo cáo | **Thời gian:** 10/03/2026 15:30 / **Trạng thái:** Đã tiếp nhận / **Người thực hiện:** Nguyễn Văn A - Lãnh đạo Khu CN Hải Phòng / **Action:** Phê duyệt và gửi báo cáo đến Cục đầu tư nước ngoài |
| 5 | Chờ duyệt | Chờ duyệt | Khi các người dùng/ cơ quan trung gian duyệt để đẩy báo cáo sang người dùng/ cơ quan trung gian tiếp theo | **Thời gian:** 10/03/2026 15:30 / **Trạng thái:** Chờ duyệt / **Người thực hiện:** Nguyễn Văn A - Cán bộ tổng hợp khu CN Hải Phòng / **Action:** Phê duyệt và gửi báo cáo đến Lãnh đạo khu CN Hải Phòng |
| 6 | Chờ duyệt | Yêu cầu chỉnh sửa | Khi các người dùng/ cơ quan trung gian từ chối báo cáo | **Thời gian:** 10/03/2026 15:30 / **Trạng thái:** Yêu cầu chỉnh sửa / **Người thực hiện:** Nguyễn Văn A - Cán bộ Tổng hợp khu CN Hải Phòng / **Action:** Từ chối báo cáo / **Lý do:** Thông tin X chưa chính xác |
| 7 | Đã tiếp nhận | Yêu cầu chỉnh sửa | Cơ quan tiếp nhận cuối cùng từ chối | **Thời gian:** 10/03/2026 15:30 / **Trạng thái:** Yêu cầu chỉnh sửa / **Người thực hiện:** Nguyễn Văn A - Cán bộ Chuyên môn Cục đầu tư nước ngoài / **Action:** Từ chối báo cáo / **Lý do:** Thông tin X chưa chính xác |
| 8 | Đã tiếp nhận | Đã tiếp nhận | Cơ quan tiếp nhận báo cáo cuối cùng có thể tự chỉnh sửa; báo cáo vẫn ở trạng thái Đã tiếp nhận | **Thời gian:** 10/03/2026 15:30 / **Trạng thái:** Đã tiếp nhận / **Người thực hiện:** Nguyễn Văn A - Lãnh đạo Cục đầu tư nước ngoài / **Action:** Chỉnh sửa báo cáo / **Ảnh data snapshot:** trước chỉnh sửa và sau chỉnh sửa |
| 9 | Yêu cầu chỉnh sửa | Chờ duyệt | Khi user sửa báo cáo và ấn Nộp báo cáo (với trường hợp quy trình có > 2 bước) | **Thời gian:** 10/03/2026 15:30 / **Trạng thái:** Chờ duyệt / **Người thực hiện:** Nguyễn Văn A - Nhà đầu tư / **Action:** Thực hiện chỉnh sửa và nộp lại / **Ảnh data snapshot:** trước chỉnh sửa và sau chỉnh sửa |
| 10 | Yêu cầu chỉnh sửa | Đã tiếp nhận | Khi user sửa báo cáo và ấn Nộp báo cáo (với trường hợp quy trình có 2 bước) | **Thời gian:** 10/03/2026 15:30 / **Trạng thái:** Đã tiếp nhận / **Người thực hiện:** Nguyễn Văn A - Nhà đầu tư / **Action:** Thực hiện chỉnh sửa và nộp lại / **Ảnh data snapshot:** trước chỉnh sửa và sau chỉnh sửa |
| 11 | Yêu cầu chỉnh sửa | Yêu cầu chỉnh sửa | Khi user chỉnh sửa báo cáo bị từ chối nhưng chỉ lưu nháp | **Thời gian:** 10/03/2026 15:30 / **Trạng thái:** Yêu cầu chỉnh sửa / **Người thực hiện:** Nguyễn Văn A - Nhà đầu tư / **Action:** Thực hiện chỉnh sửa và lưu nháp / **Ảnh data snapshot:** trước chỉnh sửa và sau chỉnh sửa |
| 12 | (Không có) | Lưu nháp | Người dùng Tạo mới báo cáo và lưu nháp | **Thời gian:** 10/03/2026 15:30 / **Trạng thái:** Lưu nháp / **Người thực hiện:** Nguyễn Văn A - Nhà đầu tư / **Action:** Tạo mới báo cáo và lưu nháp |

### Xử lý lỗi

- Lỗi tải dữ liệu Timeline: Hiển thị Toast lỗi — Tiêu đề: *"Lỗi hệ thống"*, Nội dung: *"Không thể kết nối đến hệ thống. Vui lòng thử lại sau."*

---

<mark>

## CF_06.1: Áp dụng cho Báo cáo gộp — Xem vòng đời (CF_06)

> **Bổ sung mới — 2026-04-21 | UC011-034**

- **Scope timeline:** Vòng đời áp dụng ở **cấp Bộ hồ sơ** — 1 timeline chung cho toàn package (không phải từng biểu riêng lẻ).
- Timeline ghi nhận các sự kiện cấp package: Tạo mới, Lưu nháp (biểu X), Nộp, Yêu cầu chỉnh sửa.

> ⏳ **[PENDING — CHL-09]:** Chi tiết các loại hành động trong timeline Báo cáo gộp (tên event, log biểu nào được lưu v.v.) sẽ được BA xác nhận và cập nhật trong sprint sau.

</mark>

---

## CF_07: Xem chi tiết (View Detail — Full-Page Screen)

### Mô tả

Hiển thị toàn bộ thông tin báo cáo dưới dạng màn hình xem toàn trang (full-page), read-only. Giao diện giống hệt màn hình Chỉnh sửa (CF_03) nhưng toàn bộ trường bị Disabled — người dùng không thể nhập hay chỉnh sửa bất kỳ dữ liệu nào.

### Điều kiện hiển thị nút [Xem chi tiết]

Nút [Xem chi tiết] hiển thị ở tất cả trạng thái bản ghi, cho tất cả người dùng có quyền xem. Tham chiếu: CMR_03.

### Nguồn kích hoạt

Từ màn hình Danh sách → Cột Hành động → Nhấn nút [Xem chi tiết] → Hệ thống điều hướng sang màn hình Xem toàn trang (không phải popup).

### Luồng nghiệp vụ

- **Bước 1:** Người dùng nhấn nút [Xem chi tiết] tại cột Hành động trên Danh sách.
- **Bước 2:** Hệ thống điều hướng sang màn hình Xem chi tiết (full-page view screen).
- **Bước 3:** Form hiển thị toàn bộ dữ liệu đã lưu của bản ghi. Toàn bộ trường ở trạng thái Disabled.
- **Bước 4:** Người dùng có thể thực hiện một trong các thao tác:
  - Nhấn **[Xem trước]** → Xem preview PDF. Tham chiếu: CF_07.1.
  - Nhấn **[Chỉnh sửa]** → Điều hướng sang màn hình Chỉnh sửa (CF_03). *(Chỉ hiển thị nếu đủ điều kiện — xem mục "Nút [Chỉnh sửa]" bên dưới.)*
  - Nhấn **[Hủy]** → Quay về màn hình Danh sách.

### Nút [Chỉnh sửa]

- **Điều kiện hiển thị:** Hiển thị khi bản ghi ở trạng thái **Lưu nháp** hoặc **Yêu cầu chỉnh sửa**. Tham chiếu: CMR_03.
  - Case A (ĐTNN/ĐTTN — CMR_01): Chỉ TCKT phụ trách mới thấy nút [Chỉnh sửa]. Các NĐT thành viên chỉ có quyền Xem — không thấy nút này.
  - Case B (ĐTRNN — CMR_02): Tất cả NĐT trong dự án (kể cả NĐT không phải người khởi tạo) đều thấy và có thể nhấn nút [Chỉnh sửa].
- **Nếu không thỏa mãn điều kiện trạng thái:** Ẩn hoàn toàn nút [Chỉnh sửa].
- **Khi nhấn:** Điều hướng sang màn hình Chỉnh sửa (CF_03).

### Nút [Hủy]

- Điều hướng về màn hình Danh sách.
- Không cần popup xác nhận (người dùng chỉ xem, không có dữ liệu chưa lưu).

### CF_07.1: Popup PDF Preview (kích hoạt bởi nút [Xem trước])

- Mở popup hiển thị dữ liệu bản ghi theo định dạng PDF (Read-only).
- Popup có icon Đóng (✕) ở góc trên bên phải thanh tiêu đề. Nhấn → Đóng popup, quay lại màn hình trước đó.
- Nội dung: Vùng xem preview biểu mẫu theo đúng format PDF (có thanh cuộn).
- Khu vực footer: 1 nút hành động:
  - **[In]:** Mở Print Preview dạng PDF → mở hộp thoại in trình duyệt.

### Phạm vi popup PDF Preview

Popup PDF Preview **chỉ** được truy cập từ bên trong 3 màn hình:

- Màn hình Tạo mới (CF_01) — thông qua nút [Xem trước]
- Màn hình Chỉnh sửa (CF_03) — thông qua nút [Xem trước]
- Màn hình Xem chi tiết (CF_07) — thông qua nút [Xem trước]

Popup này **không** được trigger trực tiếp từ cột Hành động trên màn hình Danh sách.

### Edge cases

- Lỗi tải dữ liệu màn hình View → Toast lỗi — Tiêu đề: *"Lỗi hệ thống"*, Nội dung: *"Không thể kết nối đến hệ thống. Vui lòng thử lại sau."*
- Lỗi xuất báo cáo trong popup Preview → Toast lỗi — Tiêu đề: *"Lỗi hệ thống"*, Nội dung: *"Không thể kết nối đến hệ thống. Vui lòng thử lại sau."*

---

## CF_08: Xóa báo cáo (Delete Report)

### Mô tả

Cho phép người dùng xóa bản ghi báo cáo tạm thời khỏi hệ thống. Chức năng này chỉ áp dụng cho các bản ghi **chưa từng trải qua bất kỳ quy trình nộp nào**.

### Điều kiện hiển thị nút [Xóa]

Nút [Xóa] chỉ hiển thị khi **đồng thời** thỏa mãn cả hai điều kiện sau:

1. Bản ghi đang ở trạng thái **Lưu nháp (Draft)**. Tham chiếu: CMR_03.
2. Bản ghi **chưa từng được nộp lần nào** — không tồn tại lịch sử nộp trong Audit Trail (vòng đời bản ghi).

> **Lưu ý Lifecycle Lock:** Ngay khi bản ghi đã từng chuyển sang trạng thái Chờ duyệt / Đã tiếp nhận hoặc Yêu cầu chỉnh sửa — dù sau đó có được chỉnh sửa và quay về trạng thái Lưu nháp — nút [Xóa] vẫn bị **ẩn vĩnh viễn, không phục hồi**.

### Phân quyền

Hệ thống áp dụng 2 mô hình phân quyền tùy theo loại dự án:

| Loại dự án                  | Đối tượng               | Quyền                                                                                             |
| ------------------------------ | --------------------------- | -------------------------------------------------------------------------------------------------- |
| **ĐTNN/ĐTTN** (CMR_01) | TCKT phụ trách            | Thấy và có thể nhấn [Xóa], [Chỉnh sửa]                                                     |
| **ĐTNN/ĐTTN** (CMR_01) | NĐT thành viên           | **Không thấy** nút [Xóa] và [Chỉnh sửa] — chỉ có quyền Xem                        |
| **ĐTRNN** (CMR_02)      | Tất cả NĐT trong dự án | Đều thấy và có thể nhấn [Xóa], [Chỉnh sửa] nếu bản ghi thỏa điều kiện trạng thái |

Thao tác Xóa của bất kỳ NĐT nào đều được ghi vào Lifecycle Log kèm tên tài khoản và thời gian thực hiện. Tham chiếu: CMR_02.

### Luồng tương tác

- **Bước 1:** Người dùng nhấn nút [Xóa] tại cột Hành động trên màn hình Danh sách.
- **Bước 2:** Hệ thống hiển thị Popup xác nhận (P04) với nội dung:
  - Nội dung: *"Bạn có chắc chắn muốn xóa báo cáo này?"*
  - Nút **[Đồng ý]** / Nút **[Hủy]**.
- **Bước 3 — Nếu chọn [Đồng ý]:** Bản ghi bị xóa khỏi danh sách. Hệ thống hiển thị Toast thành công (T08) — Tiêu đề: *"Thành công"*, Nội dung: *"Xóa báo cáo thành công"*.
- **Bước 3 — Nếu chọn [Hủy]:** Đóng popup và giữ nguyên trạng thái bản ghi. Không có thay đổi nào được thực hiện.

### Xử lý lỗi

- Lỗi server khi xóa → Toast lỗi — Tiêu đề: *"Lỗi hệ thống"*, Nội dung: *"Không thể kết nối đến hệ thống. Vui lòng thử lại sau."* Bản ghi không bị xóa, giữ nguyên trạng thái.

---

<mark>

## CF_09: Xử lý nút [Nộp] từ màn hình Danh sách (Listing → Submit)

> **Bổ sung mới — 2026-04-21 | UC011-034**

### Mô tả

Chức năng cho phép người dùng kích hoạt luồng Nộp báo cáo/Bộ hồ sơ trực tiếp từ cột Hành động trên màn hình Danh sách, không cần mở lại màn hình Lập báo cáo. Áp dụng cho **TẤT CẢ** loại báo cáo (đơn lẻ và Báo cáo gộp).

### Điều kiện hiển thị nút [Nộp] từ Màn hình danh sách

- Bản ghi/Bộ hồ sơ ở trạng thái **Lưu nháp** hoặc **Yêu cầu chỉnh sửa**. Tham chiếu: CMR_03.
- **Phân quyền theo loại dự án:**
  - **ĐTNN/ĐTTN (CMR_01):** Chỉ TCKT phụ trách mới thấy nút [Nộp].
  - **ĐTRNN (CMR_02):** Tất cả NĐT trong dự án đều thấy và có thể nhấn nút [Nộp] (nếu bản ghi thỏa điều kiện trạng thái).

### Trạng thái nút [Nộp] theo trạng thái bản ghi

- **Trạng thái "Lưu nháp":** Nút [Nộp] luôn **Enabled**.
- **Trạng thái "Yêu cầu chỉnh sửa":** Nút [Nộp] mặc định **Disabled** (mờ, không thể nhấn). Hiển thị tooltip khi hover: *"Vui lòng chỉnh sửa báo cáo trước khi nộp lại."* Nút chỉ chuyển sang **Enabled** sau khi người dùng đã vào Chỉnh sửa, thay đổi ít nhất 1 trường, và Lưu nháp thành công. Tham chiếu: CMR_14.

### Luồng nghiệp vụ

- **Bước 1:** Người dùng nhấn [Nộp] tại cột Hành động trên màn hình Danh sách.
- **Bước 2:** Hệ thống validate toàn bộ dữ liệu hiện tại của báo cáo/Bộ hồ sơ.
- **Bước 3a — Nếu PASS:** Hiển thị Popup xác nhận Nộp. Luồng từ đây giống hệt mục "Xử lý nút [Nộp báo cáo]" trong CF_01.
- **Bước 3b — Nếu FAIL:** Mở màn hình Chỉnh sửa báo cáo (CF_03) và hiển thị lỗi tương ứng:
  - **[Báo cáo gộp]:** Hiển thị badge/indicator đỏ trên tab header của tab có lỗi. Lỗi inline màu đỏ dưới từng trường vi phạm. Hệ thống scroll/focus vào vị trí lỗi đầu tiên.
  - **[Báo cáo đơn lẻ]:** Hiển thị lỗi inline màu đỏ dưới từng trường vi phạm. Hệ thống scroll/focus vào vị trí lỗi đầu tiên.
  - **Hành vi sau khi sửa lỗi:** Người dùng ở lại màn hình Chỉnh sửa. Sau khi Lưu nháp thành công, giữ nguyên ở màn hình hiện tại (không quay lại Danh sách). Tham chiếu: CF_01.

</mark>

---

## 4. Lịch sử cập nhật

| Ngày      | Phiên bản  | Mục cập nhật                                | Before                                                                                              | After                                                                                                                       | Ghi chú                                                    |
| ---------- |------------| ---------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| 2026-05-03 | 1.0 → 1.1  | CF_01, CF_03, CF_08                            | Trạng thái: Đã nộp                                                                             | Trạng thái: Chờ duyệt / Đã tiếp nhận                                                                                | Thay đổi theo bộ trạng thái mới                       |
| 2026-05-04 | 1.1 → 1.2  | CF_02, CF_04                                   | Tên file                                                                                           | Bổ sung quy tắc đặt tên                                                                                                | Thêm rule naming convention cho file Nhập từ file và Xuất báo cáo     |
| 2026-05-05 | 1.2 → 1.3  | CF_01 — Xử lý nút [Hủy]                   | Popup: "Bạn có chắc muốn hủy? Dữ liệu chưa lưu sẽ bị mất." / Nút [Xác nhận] / [Hủy] | Popup: "Dữ liệu chưa được lưu" / Nút [Đồng ý] / [Hủy]. Thêm dirty check. Tham chiếu CMR_14                    | Đồng bộ popup theo CMR_14                                |
| 2026-05-05 | 1.2 → 1.3  | CF_01.1 — Dirty Form Guard tab nội bộ       | (Không có)                                                                                        | Thêm mô tả: popup cảnh báo khi chuyển tab biểu mẫu nội bộ trong báo cáo gộp. Tham chiếu CMR_14                | Áp dụng CMR_14 cho báo cáo gộp                         |
| 2026-05-05 | 1.2 → 1.3  | CF_03 — Xử lý nút [Hủy]                   | Popup: "Bạn có chắc muốn hủy? Dữ liệu chưa lưu sẽ bị mất." / Nút [Xác nhận] / [Hủy] | Popup: "Dữ liệu chưa được lưu" / Nút [Đồng ý] / [Hủy]. Thêm dirty check. Tham chiếu CMR_14                    | Đồng bộ popup theo CMR_14                                |
| 2026-05-05 | 1.3 → 1.4  | CF_02 — Điều kiện hiển thị nút [Nhập từ file] | Kỳ hạn "Trong thời hạn" hoặc "Qua kỳ báo cáo" → Hiển thị. "Chưa tới hạn" → Ẩn.      | Kỳ hạn "Trong thời hạn" → Hiển thị. "Chưa tới hạn" hoặc "Qua kỳ báo cáo" → Ẩn. Không được phép nhập từ file. | Đồng bộ với CF_01: quá hạn chặn cả Lập lẫn Nhập từ file |
| 2026-05-08 | 1.4 → 1.5  | CF_01.1 — Trạng thái nộp Báo cáo gộp | chuyển trạng thái sang "Đã nộp" | chuyển trạng thái sang "Chờ duyệt" hoặc "Đã tiếp nhận" (theo CMR_03) | Fix sót từ đợt cập nhật status |
| 2026-05-08 | 1.5 → 1.6  | CF_01.1 — Lưu nháp Báo cáo gộp | Không nêu rõ redirect | Giữ nguyên ở màn hình hiện tại (không quay lại Danh sách) | Khác CF_01 (đơn lẻ quay lại DS) |
| 2026-05-08 | 1.5 → 1.6  | CF_01.1 — Chuyển tab nội bộ | Mâu thuẫn: vừa popup vừa giữ in-memory | Popup khi dirty, không popup khi vừa lưu hoặc chưa sửa. Xóa phần in-memory mâu thuẫn | Đồng bộ với CMR_14 báo cáo gộp |
| 2026-05-08 | 1.6 → 1.7  | CF_01, CF_01.1, CF_03 — Validate Lưu nháp | Mô tả không rõ ràng, trộn 2 case | Phân rõ 2 case: (1) CÓ Phạm vi → bắt buộc chọn Phạm vi; (2) KHÔNG CÓ Phạm vi → ít nhất 1 trường có data | Làm rõ logic tối thiểu cho Lưu nháp |
| 2026-05-08 | 1.7 → 1.8  | CF_01, CF_01.1 — Tên nút Submit | Nộp báo cáo (10 lần) | Nộp báo cáo | Thống nhất tên nút toàn hệ thống |
| 2026-05-12 | 1.8 → 1.9  | CF_01.1 — Lưu nháp scope | Lưu nháp chỉ lưu tab đang mở | Lưu nháp lưu toàn bộ N tabs cùng lúc. Validate từng tab độc lập. Toast: "Đã lưu Bộ hồ sơ thành công" | Thay đổi scope lưu nháp Báo cáo gộp |
| 2026-05-12 | 1.8 → 1.9  | CF_01.1 — Chuyển tab nội bộ | Popup Dirty Form Guard khi chuyển tab | Bỏ popup chuyển tab. Dữ liệu giữ in-memory khi chuyển tab tự do. Popup chỉ hiển thị khi rời màn hình (nút [Hủy]) | Dữ liệu in-memory → không mất khi chuyển tab |
| 2026-05-12 | 1.8 → 1.9  | CF_01.1 — Nút [Hủy] Báo cáo gộp | Dirty check không rõ scope | Dirty check toàn bộ N tabs. Bất kỳ tab nào dirty → hiển thị popup cảnh báo rời trang | Bổ sung mục [Hủy] riêng cho Báo cáo gộp |
| 2026-05-13 | 1.9 → 2.0  | CF_01, CF_03 — Nút [Xem chi tiết] | Không có rule disable/enable | Nút [Xem chi tiết] Disabled tại màn hình Lập khi chưa Lưu nháp/Nộp lần nào. Enabled sau khi bản ghi đã tồn tại trong DB. CF_03 và CF_07 luôn Enabled. | Yêu cầu mới từ BA |
| 2026-05-17 | 2.0 -> 2.1 | CF_01/CF_01.1/CF_03 Required messages | Truong bat buoc (5 vi tri) | Vui long chon/nhap [ten truong] + tham chieu CMR_05/06/07 | Dong bo CMR v2.0 |
| 2026-05-18 | 2.1 -> 2.2 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-15 | 2.0 → 2.1  | CF_06 — Luồng nghiệp vụ | Sắp xếp theo thứ tự thời gian tăng dần (cũ nhất ở trên, mới nhất ở dưới) | Bổ sung mô tả scope timeline + sắp xếp theo thời gian giảm dần (mới nhất ở trên, cũ nhất ở dưới) | Cập nhật theo tài liệu Lifecycle |
| 2026-05-15 | 2.0 → 2.1  | CF_06 — Cấu trúc popup (Nội dung Timeline) | 3 bullet: Thời gian thao tác, Tài khoản thực hiện, Hành động (Chưa xác định) | Thay thế bằng Bảng thành phần log (6 thành phần) + Bảng chú thích format hành động (12 cases) + lazy load + link Figma | Cập nhật theo tài liệu Lifecycle |
| 2026-05-15 | 2.0 → 2.1  | CF_06 — Giải thích các trạng thái | (Không có) | Thêm mới mục "Giải thích các trạng thái" với bảng 12 trường hợp chuyển trạng thái kèm ví dụ log | Cập nhật theo tài liệu Lifecycle |
| 2026-05-17 | 2.1 -> 2.2 | CF_01/CF_01.1/CF_03 Required messages | Truong bat buoc (5 vi tri) | Vui long chon/nhap [ten truong] + tham chieu CMR_05/06/07 | Dong bo CMR v2.0 |
| 2026-05-18 | 2.2 -> 2.3 | CS_01 Mục 2 — YearPicker behavior (tham chiếu) | YearPicker disable các năm không có data | YearPicker enable toàn bộ các năm; năm không có data → Empty State "Không có dữ liệu". Tham chiếu: CS_01 Mục 2 (v1.7) | Bỏ logic disable năm theo yêu cầu UX |
| 2026-05-20 | 2.3 -> 2.4 | CF_09 — Phân quyền nút [Nộp] | Chỉ "người đã khởi tạo" mới thấy nút [Nộp] | Phân quyền theo loại dự án: ĐTNN/ĐTTN → TCKT phụ trách; ĐTRNN → tất cả NĐT. Tham chiếu: CMR_01, CMR_02 | Đồng bộ CF_09 với CMR_02 |
| 2026-05-20 | 2.3 -> 2.4 | CF_09 — Disable nút [Nộp] trạng thái YC chỉnh sửa | Nút [Nộp] luôn Enabled khi hiển thị | Nút [Nộp] Disabled khi trạng thái "YC chỉnh sửa" + chưa chỉnh sửa. Tooltip: "Vui lòng chỉnh sửa báo cáo trước khi nộp lại." Tham chiếu: CMR_14 | Giải quyết conflict CF_09 vs CMR_03 |
| 2026-05-20 | 2.3 -> 2.4 | CF_03 — Disable [Nộp]/[Lưu nháp] khi YC chỉnh sửa | Nút luôn Enabled | Disabled khi form chưa dirty + trạng thái "YC chỉnh sửa". Tooltip hướng dẫn. Enable ngay khi form dirty. Tham chiếu: CMR_14 | Đồng bộ logic dirty form với CMR_14 |
| 2026-05-20 | 2.3 -> 2.4 | CF_06 STT 11 — Trạng thái sau Lưu nháp | Trạng thái sau: "Lưu nháp" | Trạng thái sau: "Yêu cầu chỉnh sửa" (giữ nguyên, không chuyển) | Đồng nhất với CF_03 quy tắc bảo toàn trạng thái |
| 2026-05-20 | 2.3 -> 2.4 | CF_01, CF_03 — Redirect sau Lưu nháp | Quay lại màn hình Danh sách | Giữ nguyên ở màn hình hiện tại | Đồng nhất với CF_01.1 (Báo cáo gộp) |
| 2026-05-21 | 2.4 → 2.5 | CF_06 — Màn hình tham chiếu | `- Màn hình tham chiếu: https://www.figma.com/design/rGEYT2z6vyTy0Bcr3jsIgw/Untitled?node-id=101-1633&t=0sO6ntxlIdXCjmoV-4` | `- Màn hình tham chiếu: https://www.figma.com/design/cklcaM2w5S8To691104P3j/C%E1%BB%95ng-%C4%91%E1%BA%A7u-t%C6%B0-QG---B%C3%A1o-c%C3%A1o?node-id=8211-1000&t=qpm0MOdtCsoqAgcQ-4` | Cập nhật đường link Figma màn hình tham chiếu theo yêu cầu |
| 2026-05-23 | 2.5 → 2.6 | CF_02 — Case 1: Báo cáo có Phạm vi dữ liệu nguồn input bắt buộc | Mô tả chung, không phân loại Single/Multi-scope, dropdown không rõ dạng | Phân loại Single-scope/Multi-scope, dropdown single/multiple choice, hệ thống phân loại theo section, rule thêm/bớt phạm vi quay lại Bước 1, trường Master Data bị khóa | Bổ sung chi tiết phân loại phạm vi và logic Multi-scope |
| 2026-05-24 | 2.6 → 2.7 | CF_01, CF_03, CF_07.1 — Popup Preview footer | 2 nút: [In] + [Xuất báo cáo] | 1 nút: chỉ **[In]**. Bỏ [Xuất báo cáo] khỏi popup Preview. Xuất báo cáo chỉ từ Danh sách (CF_04) | Align theo Align_CMR_Report rule I-bis |
