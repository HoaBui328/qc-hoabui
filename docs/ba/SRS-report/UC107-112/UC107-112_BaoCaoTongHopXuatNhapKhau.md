# UC107-112: Báo cáo tổng hợp tình hình xuất, nhập khẩu của tổ chức kinh tế có vốn đầu tư nước ngoài năm ...

| Thuộc tính                          | Giá trị                                         |
| ------------------------------------- | ------------------------------------------------- |
| **BA phụ trách**              | yen.le2                                           |
| **Phân hệ**                   | Quản lý đầu tư nước ngoài vào Việt Nam |
| **Mẫu biểu**                  | Mẫu A.IV.8.a                                     |
| **Loại báo cáo**             | Định kỳ năm                                   |
| **Phạm vi báo cáo**           | Không có phạm vi                                              |
| **Hình thức nộp**            | Báo cáo đơn lẻ (Single report form)          |
| **Cơ quan nhận**              | Cục Đầu tư nước ngoài, Bộ Tài chính     |
| **Đối tượng lập**          | Cục Hải quan / Bộ Tài chính                  |
| **Giao diện**                  | Admin site                                        |
| **Ngày tạo**                  | 2026-05-05                                        |
| **Phiên bản**                 | 1.4                                               |
| **Quy tắc sinh mã báo cáo** | FDI_AIV8A_[ID]                                   |
| **Loại quy trình**           | Quy trình 3 bước, CMCĐT_BCTK_09                 |

> **Lưu ý kiến trúc:** Mẫu A.IV.8a là báo cáo **tổng hợp (Aggregation)** từ Mẫu 8b (Xuất khẩu) và 8c (Nhập khẩu). Hệ thống cung cấp nút [Tổng hợp dữ liệu] cho phép người dùng **tự chọn bản ghi nguồn** để tổng hợp. Hệ thống thực hiện **Group By Tỉnh/TP** và **SUM giá trị** để điền vào bảng.
> - **Bảng Fixed 34 Rows** — bảng mặc định hiển thị **34 dòng** theo danh sách 34 tỉnh/thành phố (sáp nhập mới). Không cho phép thêm hoặc xóa dòng.
> - Mỗi Tỉnh/TP chỉ xuất hiện đúng 1 lần (unique, cố định).
> - Khi tổng hợp, hệ thống điền giá trị vào dòng tương ứng. Tỉnh/TP không có dữ liệu → giá trị = 0.
> - User có thể chỉnh sửa dữ liệu sau khi tổng hợp.

---

## UC107-112.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Xem danh sách báo cáo tổng hợp tình hình xuất, nhập khẩu của tổ chức kinh tế có vốn đầu tư nước ngoài (Mẫu A.IV.8a)
- Chức năng cho phép cán bộ Cục Hải quan truy cập màn hình chính để theo dõi danh sách các báo cáo tổng hợp hàng năm. Mục tiêu: Hỗ trợ đơn vị nộp báo cáo trực tuyến, thuận tiện trong việc lấy, kiểm duyệt, lưu trữ dữ liệu và theo dõi lịch sử phê duyệt.
- Out of scope: Không cho phép nộp báo cáo khi đã quá hạn kỳ báo cáo. Chức năng duyệt báo cáo được thực hiện ở các UC duyệt báo cáo chung.

Phân quyền: Cục Hải quan / Bộ Tài chính. Tham chiếu: CMR_02.

**Tiền điều kiện (Preconditions):**
- Tài khoản người dùng có quyền lập/xem báo cáo thuộc đơn vị Cục Hải quan.
- Kỳ báo cáo năm tương ứng đang ở trạng thái "Trong thời hạn".

**Hậu điều kiện (Postconditions):**
- Sau khi Nộp báo cáo thành công, hệ thống gửi thông báo (Notification) cho đơn vị cấp trên (Cục ĐTNN).
- Thao tác Xóa báo cáo (soft-delete) được lưu Audit log để tra soát.

Truy cập chức năng: Phân hệ Báo cáo → Quản lý ĐTNN vào VN → Báo cáo tổng hợp tình hình xuất, nhập khẩu của TCKT có vốn ĐTNN (Mẫu A.IV.8a)

Chức năng đáp ứng usecase số: 107, 108, 109, 110, 111, 112

---

### 2. Mô tả giao diện

**Giao diện danh sách**

Giao diện: **Flat-list** (Site Admin) — Danh sách phẳng, không nhóm theo kỳ hạn.

Mô tả giao diện:

| #                                              | Tên trường           | Kiểu trường              | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả                                                                                                                                                                                          |
| ---------------------------------------------- | ----------------------- | --------------------------- | --------------------- | ------------ | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Khung Điều kiện Lọc & Tìm kiếm** |                         |                             |                       |              |            |                                                                                                                                                                                                  |
| 1                                              | Năm báo cáo          | Yearpicker                  | Năm hiện tại       | x            |            | Người dùng chọn năm; hệ thống lọc danh sách theo năm. Kết quả hiển thị ngay lập tức. Tham chiếu: CMR_07.                                                                        |
| 2                                              | Trạng thái báo cáo  | Multiple-selection Dropdown | Tất cả                | x            |            | Người dùng chọn một hoặc nhiều giá trị: Tất cả / Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_03, CMR_07., CMR_16 |
| 3                                              | Mã báo cáo           | Search bar                  | Null                  | x            |            | Tìm theo mã báo cáo. Kết quả hiển thị ngay khi nhập. Nếu không tìm thấy: hiển thị "Không tìm thấy kết quả". Tham chiếu: CMR_06, CMR_09. Placeholder: "Tìm kiếm nhanh theo mã báo cáo".     |
| **Khung Danh sách Báo cáo**           |                         |                             |                       |              |            |                                                                                                                                                                                                  |
| 4                                              | Mã báo cáo           | Label                       | Null                  |              |            | Hiển thị mã báo cáo (FDI_AIV8A_XXX). Tham chiếu: CMR_09.                                                                                                                                  |
| 5                                              | Năm báo cáo          | Label                       | Null                  |              |            | Hiển thị năm báo cáo.                                                                                                                                                                       |
| 6                                              | Ngày cập nhật | Label                       | Null                  |              |            | Hiển thị ngày giờ nộp hoặc cập nhật gần nhất. Định dạng: dd/MM/yyyy HH:mm.                                                                                                          |
| 7                                              | Trạng thái báo cáo  | Label                       | Null                  |              |            | Trạng thái cấp bản ghi. Tham chiếu: CMR_03.                                                                                                                                                 |
| 8                                              | Hành động            | Button group                | Null                  |              |            | Các nút thao tác theo trạng thái: Xem, Sửa, Xóa, In, Xuất báo cáo, Vòng đời. Chi tiết tại UC107-112.3.                                                                                     |

---

### 3. Mô tả các xử lý của chức năng

- Thao tác lọc & tìm kiếm: Kết quả hiển thị ngay lập tức sau khi người dùng tương tác. Tham chiếu: CMR_07.
- Sắp xếp giảm dần theo năm (mới nhất lên đầu).
- Phân trang: Mặc định 10 bản ghi/trang. Tham chiếu: CMR_10.

---

## UC107-112.2: Lập Báo Cáo (Tổng hợp dữ liệu)

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Tạo mới/Chỉnh sửa báo cáo tổng hợp tình hình xuất, nhập khẩu (Mẫu A.IV.8.a)
- Chức năng cho phép cán bộ thực hiện tổng hợp số liệu từ Mẫu 8b (Chi tiết xuất khẩu) và Mẫu 8c (Chi tiết nhập khẩu) đã được các đơn vị nộp.

Phân quyền: Cán bộ Cục Hải quan, Bộ Tài chính.

Truy cập chức năng: Màn danh sách báo cáo (UC107-112.1) → Nhấn nút [Lập báo cáo]

Chức năng đáp ứng usecase số: 107, 108

---

### 2. Mô tả giao diện

Giao diện: Màn hình nhập liệu theo biểu mẫu A.IV.8.a.

Mô tả giao diện:

| #                                    | Tên trường               | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Ghi chú                                                                                                                                                                           |
| ------------------------------------ | --------------------------- | -------------- | --------------------- | ------------ | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **THÔNG TIN CHUNG**           |                             |                |                       |              |            |                                                                                                                                                                                    |
| 1                                    | Năm báo cáo              | Yearpicker     | Năm hiện tại       |             | x          | Hiển thị năm báo cáo đã chọn từ màn danh sách. **Disabled** — không cho sửa. Tham chiếu: CMR_05.                                                                                                                                   |
| 2                                    | Nút [Tổng hợp dữ liệu] | Button         |                       |              |            | Nhấn để thực hiện logic tổng hợp từ Mẫu 8b và 8c. Chi tiết xử lý tại mục 3.                                                                                         |
| **BẢNG SỐ LIỆU TỔNG HỢP (Fixed 34 Rows)** |                             |                |                       |              |            | Bảng cố định 34 dòng theo danh sách 34 tỉnh/thành phố (sáp nhập mới). Không cho phép thêm hoặc xóa dòng. |
| 3                                    | STT                         | Integer        | Auto                  |              |            | Hệ thống tự đánh số tăng dần từ 1 đến 34. Disabled. |
| 4                                    | Địa phương              | Label       | Từ danh mục 34 tỉnh/TP                  |             |           | Hiển thị tên tỉnh/thành phố theo danh sách 34 đơn vị hành chính (sáp nhập mới). Disabled — không cho sửa. Thứ tự mặc định theo mã đơn vị hành chính. |
| 5                                    | Giá trị xuất khẩu (USD) | Decimal        | 0                  | x            | x          | Tổng giá trị xuất khẩu từ Mẫu 8b của địa phương tương ứng. Auto-fill từ tổng hợp, cho phép chỉnh sửa. Validate: >= 0. Decimal: tối đa 5 chữ số thập phân. Tham chiếu: CMR_05. |
| 6                                    | Giá trị nhập khẩu (USD) | Decimal        | 0                  | x            | x          | Tổng giá trị nhập khẩu từ Mẫu 8c của địa phương tương ứng. Auto-fill từ tổng hợp, cho phép chỉnh sửa. Validate: >= 0. Decimal: tối đa 5 chữ số thập phân. Tham chiếu: CMR_05. |
| **DÒNG TỔNG CỘNG**          |                             |                |                       |              |            |                                                                                                                                                                                    |
| 7                                    | Tổng xuất khẩu (USD)     | Calculated     | Auto                  |              |            | = SUM dọc toàn bộ cột Giá trị xuất khẩu (field #5). Disabled. Decimal: tối đa 5 chữ số thập phân. Cập nhật real-time.                                                                                        |
| 8                                    | Tổng nhập khẩu (USD)     | Calculated     | Auto                  |              |            | = SUM dọc toàn bộ cột Giá trị nhập khẩu (field #6). Disabled. Decimal: tối đa 5 chữ số thập phân. Cập nhật real-time.                                                                                        |
| **FOOTER BÁO CÁO**           |                             |                |                       |              |            |                                                                                                                                                                                    |
| 9                                    | Nơi lập báo cáo         | Label          | Từ Profile           |              |            | Tên Tỉnh/Thành phố của cơ quan nộp. Disabled. Hệ thống tự động điền. Tham chiếu: CMR_12.                                                                            |
| 10                                   | Ngày, tháng, năm         | Label          | Ngày hiện tại      |              |            | Thời gian thực của hệ thống (Current System Date). Disabled. Tham chiếu: CMR_12.                                                                                             |
| **CÁC NÚT THAO TÁC**        |                             |                |                       |              |            |                                                                                                                                                                                    |
| 11                                   | Lưu nháp                    | Button         |                       |              |            | Lưu tạm dữ liệu đã nhập/tổng hợp. Tham chiếu: CF_01.                                                                                                                       |
| 12                                   | Nộp báo cáo                 | Button         |                       |              |            | Kiểm tra validation và Nộp báo cáo. Tham chiếu: CF_01, CF_09.                                                                                                              |
| 13                                   | Hủy                         | Button         |                       |              |            | Hủy bỏ thao tác, quay lại màn hình danh sách. Tham chiếu: CF_01.                                                                                                           |


**CÁC BUTTON**

| #  | Tên           | Kiểu   | Điều kiện hiển thị | Phân quyền       | Mô tả                                                                                |
| -- | -------------- | ------- | ----------------------- | -------------------- | ------------------------------------------------------------------------------------- |
| B1 | Hủy           | Button | Luôn                   | Người tạo         | Tham chiếu: CF_01 (mục "Xử lý nút [Hủy]").                                     |
| B2 | Xem trước | Button | Luôn                   | Người tạo         | Mở popup PDF Preview báo cáo (không rời màn Lập). Tham chiếu: CF_07.1.        |
| B3 | Lưu nháp     | Button | Luôn                   | Người tạo         | Tham chiếu: CF_01 (mục "Xử lý nút [Lưu nháp]").                                |
| B4 | Nộp báo cáo | Button | Lưu nháp, Yêu cầu CS | Người tạo         | Validate toàn bộ trường bắt buộc trước khi nộp. Tham chiếu: CF_01.         |
---



### 3. Mô tả các xử lý của chức năng

**Xử lý chung:** Tham chiếu CF_01 (Lập báo cáo), CMR_18.

**Xử lý nút [Tổng hợp dữ liệu]:**

- **Logic mặc định:** Hệ thống rà quét toàn bộ các bản ghi Mẫu 8b và 8c ở trạng thái **[Đã tiếp nhận]** trong năm báo cáo đã chọn.
- **Xử lý lựa chọn nguồn:**
  - Khi nhấn nút, hệ thống hiển thị **Popup [Chọn báo cáo nguồn để tổng hợp]**.
  - **Giao diện Popup:**
    - Gồm 2 tab hoặc 2 danh sách riêng biệt: **Báo cáo xuất khẩu (Mẫu 8b)** và **Báo cáo nhập khẩu (Mẫu 8c)**.
    - Danh sách hiển thị tất cả các báo cáo đã tồn tại trong kỳ (năm) đã chọn ở tất cả trạng thái.
    - Các cột hiển thị: Mã báo cáo, Ngày lập, Người lập, Trạng thái báo cáo.
    - Tính năng: Cho phép tìm kiếm/lọc danh sách.
  - **Quy tắc chọn:**
    - Mỗi danh sách (8b và 8c) **bắt buộc** người dùng phải chọn đúng 1 bản ghi báo cáo.
    - Hệ thống kiểm tra: Nếu chưa chọn đủ 1 bản ghi ở mỗi bên -> Nút [Xác nhận] bị Disabled hoặc báo lỗi khi nhấn.
  - Nhấn [Xác nhận] trên popup → Hệ thống thực hiện tính toán:
    - Lưu ý: Mẫu 8b và 8c là báo cáo xuất/nhập khẩu cấp trung ương đã được tổng hợp rồi.
    - `Group By`: Tỉnh/Thành phố.
    - `Sum`: Tổng tiền xuất khẩu (Mẫu 8b) và Tổng tiền nhập khẩu (Mẫu 8c).
- **Kết quả:** Hệ thống điền giá trị vào các dòng tương ứng trong bảng 34 tỉnh/TP. Nếu một tỉnh có cả xuất và nhập thì gộp vào 1 dòng. Tỉnh/TP nào không có dữ liệu từ nguồn → giá trị giữ nguyên 0. Dữ liệu sau khi tổng hợp cho phép người dùng chỉnh sửa thủ công.
- **Validate unique:** Mỗi Tỉnh/TP chỉ xuất hiện 1 lần (cố định 34 dòng, không trùng).

**Xử lý lưu và nộp:**

- **Lưu nháp:** Cho phép lưu lại kết quả đã tổng hợp hoặc đang nhập dở. Tham chiếu: CF_01.
- **Nộp báo cáo:** Validate các trường bắt buộc. Sau khi nộp, báo cáo chuyển sang trạng thái chờ duyệt. Tham chiếu: CF_01.

**Sort (Sắp xếp dòng trong bảng):**

- Cột C3 (Giá trị xuất khẩu) và C4 (Giá trị nhập khẩu) có **icon sort** trên header.
- Click icon → toggle: Ascending ↑ / Descending ↓.
- **Mặc định sort:** Theo C3 (Giá trị xuất khẩu) Descending (max → min).
- Dòng Tổng cộng luôn ở cuối bảng, không tham gia sort.
- Sort persist khi Lưu nháp → mở lại giữ nguyên thứ tự.
- Sau khi Tổng hợp dữ liệu, hệ thống auto-sort theo default sort trước khi render.

---

## UC107-112.3: Các Tác Vụ Bổ Trợ & Phê duyệt

### 1. Mô tả chức năng

Mô tả:

Phân quyền: Kiểm soát theo trạng thái bản ghi và vai trò (Người lập / Lãnh đạo). Tham chiếu: CMR_03.

---

### 2. Mô tả giao diện

**Các Button theo Action Mapping:**

| # | Tên           | Kiểu  | Điều kiện hiển thị       | Phân quyền | Mô tả                            |
| --- | --- | --- | --- | --- | --- |
| 1 | Chỉnh sửa    | Button | Lưu nháp, YC chỉnh sửa    | Người lập | Tham chiếu: CF_03                 |
| 2 | Nộp           | Button | Lưu nháp, YC chỉnh sửa    | Người lập | Tham chiếu: CF_09                 |
| 3 | Xóa           | Button | Lưu nháp (chưa từng nộp) | Người lập | Tham chiếu: CF_08                 |
| 4 | Phê duyệt    | Button | Chờ duyệt                   | Lãnh đạo  | Tham chiếu: CF_01 (mục "Duyệt") |
| 5 | YC chỉnh sửa | Button | Chờ duyệt                   | Lãnh đạo  | Tham chiếu: CF_03 (YC sửa)       |
| 6 | Xem chi tiết  | Button | Tất cả trạng thái         | Tất cả     | Tham chiếu: CF_07                 |
| 7 | In             | Button | Tất cả trạng thái         | Tất cả     | Tham chiếu: CF_05                 |
| 8 | Xuất báo cáo         | Button | Tất cả trạng thái         | Tất cả     | Tham chiếu: CF_04                 |
| 9 | Vòng đời    | Button | Tất cả trạng thái         | Tất cả     | Tham chiếu: CF_06                 |

---

### 3. Mô tả các xử lý đặc thù

- **Quy trình phê duyệt:** Theo CMR_03 cho Site Admin.
- **Xuất báo cáo:** Định dạng file Excel theo đúng Mẫu A.IV.8.a. Tham chiếu: CF_04.
- **In:** Kết xuất PDF và mở hộp thoại in. Tham chiếu: CF_05.

---

## 3.4 Acceptance Criteria (Tiêu chí nghiệm thu)

- **AC1:** Hiển thị danh sách nguồn: Nhấn "Tổng hợp dữ liệu" -> Hiển thị popup với 2 danh sách báo cáo 8b và 8c trong năm đã chọn, đầy đủ thông tin mã, ngày lập, người lập, trạng thái.
- **AC2:** Ràng buộc chọn nguồn: Nếu không chọn đủ 1 báo cáo 8b và 1 báo cáo 8c -> Không thể nhấn [Xác nhận] tổng hợp.
- **AC3:** Tính toán tổng hợp: Sau khi chọn nguồn và xác nhận -> Hệ thống Group By Tỉnh/TP, SUM giá trị → điền vào dòng tương ứng trong bảng 34 tỉnh/TP. Tỉnh không có dữ liệu → giá trị = 0.
- **AC4:** Chỉnh sửa sau tổng hợp: Người dùng có thể sửa tay các giá trị tại cột 5, 6 sau khi hệ thống đã auto-fill từ logic tổng hợp.
- **AC5:** Tính tổng cộng: Dòng tổng cộng (cột 7, 8) cập nhật chính xác tổng của cột tương ứng mỗi khi có sự thay đổi dữ liệu. Decimal: tối đa 5 chữ số thập phân.
- **AC6:** Nộp báo cáo: Nhấn "Nộp báo cáo" -> Kiểm tra validation (Năm báo cáo, dữ liệu các dòng hợp lệ) -> Thành công: Chuyển trạng thái "Chờ duyệt", gửi thông báo cho Cục ĐTNN.
- **AC7:** Fixed 34 Rows: Bảng luôn hiển thị đúng 34 dòng theo danh sách tỉnh/thành phố sáp nhập mới. Không cho phép thêm hoặc xóa dòng.
- **AC8:** Decimal precision: Cột Giá trị xuất khẩu (C3) và Giá trị nhập khẩu (C4): validate >= 0, tối đa 5 chữ số thập phân.
- **AC9 Sort:** Cột C3 (Giá trị xuất khẩu) và C4 (Giá trị nhập khẩu) có icon sort trên header. Click → toggle Ascending ↑ / Descending ↓. Mặc định sort theo C3 Descending (max → min). Dòng Tổng cộng luôn ở cuối, không tham gia sort.

---

## 3.5 Non-Functional Requirements (Yêu cầu phi chức năng)

- **Performance:** Thời gian thực hiện logic tổng hợp và hiển thị dữ liệu lên Grid < 5 giây.
- **Security:** Chỉ người dùng có thẩm quyền (Cục Hải quan/Bộ Tài chính) mới được phép thực hiện tổng hợp và nộp báo cáo mẫu này.
- **Audit:** Lưu nhật ký thay đổi đối với thao tác phê duyệt hoặc chỉnh sửa/xóa báo cáo.

---

## 4. Lịch sử cập nhật

| Ngày      | Phiên bản | Mục cập nhật       | Before | After | Ghi chú                                 |
| ---------- | ----------- | --------------------- | ------ | ----- | ---------------------------------------- |
| 2026-05-05 | 1.0         | Khởi tạo tài liệu | N/A    | N/A   | Dựa trên yêu cầu và comment của BA |
| 2026-05-06 | 1.0 → 1.1 | Objective & Scope | (Không có) | Bổ sung mục tiêu nộp trực tuyến và phạm vi. | Theo QC Audit. |
| 2026-05-06 | 1.0 → 1.1 | UI Buttons | (Không có) | Thêm nút Lưu nháp, Nộp, Hủy vào màn hình lập. | Theo QC Audit. |
| 2026-05-06 | 1.0 → 1.1 | Popup Tổng hợp | Mô tả sơ lược | Mô tả chi tiết UI popup và quy tắc chọn nguồn. | Theo phản hồi của BA. |
| 2026-05-06 | 1.0 → 1.1 | AC & NFR | (Không có) | Bổ sung 6 AC và các yêu cầu phi chức năng. | Đảm bảo tính testable. |
| 2026-05-08 | 1.1 → 1.2 | Tên nút Submit | Nộp báo cáo (1 lần) | Nộp báo cáo | Thống nhất tên nút toàn hệ thống |
| 2026-05-11 | 1.0→1.1 | Quy tắc sinh mã báo cáo | `DTNN_A4_8A_[ID]` | `FDI_AIV8A_[ID]` | Chuẩn hóa prefix và mã theo appendices.md v2.0 (INS-10) |
| 2026-05-11 | +1 | Dòng phân cách bảng Markdown | Thiếu cột (1 chỗ) | Đủ số cột theo header | Chuẩn hóa separator (INS-05) |
| 2026-05-12 | 1.1 → 1.2 | Kiến trúc bảng | Cố định 63 dòng (load sẵn 63 tỉnh/TP) | Dynamic Rows — chỉ sinh dòng cho tỉnh/TP có dữ liệu | Client confirm: chỉ tỉnh nào có số thì báo cáo. |
| 2026-05-12 | 1.1 → 1.2 | Cột Địa phương | Label (Disabled, từ CSDL) | Dropdown (chọn từ 63 tỉnh/TP, unique, auto-filter) | Chuyển từ fixed → dynamic. |
| 2026-05-12 | 1.1 → 1.2 | Thêm/Xóa dòng | Không có (63 dòng cố định) | [+ Thêm dòng] + icon Xóa dòng | Dynamic Rows cần thao tác thêm/xóa. |
| 2026-05-12 | 1.1 → 1.2 | AC | AC1-AC6 | AC1-AC9 (thêm unique, thêm dòng, empty table) | Bổ sung AC cho Dynamic Rows. |
| 2026-05-12 | 1.1 → 1.2 | Decimal precision | Không ghi rõ | 2 chữ số thập phân (cột XK, NK, dòng Tổng) | Chuẩn hóa theo biểu mẫu gốc. |
| 2026-05-14 | 1.2 → 1.3 | Kiến trúc bảng | Dynamic Rows — chỉ sinh dòng cho tỉnh/TP có dữ liệu | Fixed 34 Rows — bảng cố định 34 tỉnh/TP theo danh sách sáp nhập mới | Client confirm: danh sách 34 tỉnh thành sáp nhập. |
| 2026-05-14 | 1.3 | Cột Địa phương | Dropdown (63 tỉnh/TP, user chọn) | Label (34 tỉnh/TP cố định, Disabled) | Fixed rows — không cho sửa địa phương. |
| 2026-05-14 | 1.3 | Thêm/Xóa dòng | [+ Thêm dòng] + icon Xóa | Xóa — không cho phép thêm hoặc xóa dòng | Fixed 34 rows. |
| 2026-05-14 | 1.3 | Decimal precision | 2 chữ số thập phân | Tối đa 5 chữ số thập phân (cột XK, NK, dòng Tổng) | Client feedback. |
| 2026-05-14 | 1.3 | Sort | Không có | Icon sort C3 (XK), C4 (NK); mặc định C3 Descending (max → min) | Client feedback. |
| 2026-05-14 | 1.3 | AC | AC1-AC9 (Dynamic Rows, thêm dòng, empty table) | AC1-AC9 (Fixed 34 Rows, decimal 5dp, sort) | Viết lại AC cho Fixed Rows. |
| 2026-05-14 | 1.3 → 1.4 | Năm báo cáo (form Lập) | Editable, validate 4 chữ số | Disabled — hiển thị năm đã chọn từ màn danh sách | QC Review — năm đã chọn ở màn danh sách, không cần nhập lại. |
| 2026-05-17 | CMR v2.0 | Placeholder Search bar (1 dong) | Nhap du lieu | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 v2.0 STD-04b |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (1 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-22 | 1.4 → 1.5 | Giá trị mặc định bộ lọc Trạng thái báo cáo | Null | Tất cả + thêm option "Tất cả" vào danh sách giá trị | Tuân thủ CMR_16 — filter dropdown mặc định "Tất cả". |
